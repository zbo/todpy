// var React = require('react');

var FeatureExecutionMonitor = React.createClass({
    displayName: 'FeatureExecutionMonitor',
    getInitialState() {
    	var feature_id = $("#feature-page-header")[0].dataset['featureId'];
        return {
        	featureId: feature_id,
            logs:[]
        };
    },
    componentDidMount: function() {
        PubSub.subscribe(TOD.events.runFeature, this.requestForStartExecution);
    },
    componentWillUnmount:function() {
        PubSub.unsubscribe(this.requestForStartExecution);
    },
    requestForStartExecution:function(){
        var _url = window.location.protocol+"//"+window.location.host+"/auto/feature/exe/"+this.state.featureId+"/";
        var _self = this;

        this.setState({logs:[]});

        $.ajax({
            url:_url,
            type:"GET",
            success: function(res){
                console.log("success");
                if("result:execution already started"===res){
                    alert(res);
                    // window.clearInterval(interval_id);
                    return ;
                }
                if("result:ok"===res){
                    var _logs = _self.state.logs;
                    _logs.push("Execution Started");
                    _logs.push({
                        "content":"...",
                        "type":"content"
                    });

                    _self.setState({
                        logs: _logs
                    }); 
                    _self.pollForUpdate();   
                }
                
            },
            done: function(res){
                console.log("done");
                console.log(res);
            }
        })
        
    },
    _interval_id: -1,
    pollForUpdate: function(){
    	// poll the server for execution log
    	var _url = window.location.protocol+"//"+window.location.host+"/auto/feature/exe-status/"+this.state.featureId+"/",
            _retrieve_log_url = window.location.protocol+"//"+window.location.host+"/workspace/api/read_log/"+this.state.featureId+"/",
            _retrieve_console_output = window.location.protocol+"//"+window.location.host+"/workspace/api/read_console/"+this.state.featureId+"/";
        
        var _self = this;
        
        _self._interval_id = setInterval(function(){
            $.ajax({
                url:_url,
                type:"GET",
                success: function(res){
                    console.log("execution result");
                    console.log(res);
                    var _logs = _self.state.logs;
                    if("locked:False"===res){
                        // console.log("Run success");
                        $.ajax({
                            url: _retrieve_log_url,
                            type:"GET",
                            async: false,
                            success: function(res){
                                var lastLog = _logs.pop();

                                lastLog.content = res;

                                _logs.push(lastLog);
                                
                                _self.setState({
                                    logs: _logs
                                });         
                            },
                            fail: function(res){
                                console.log("failure");
                            }
                        });

                        
                        _logs.push("Execution Finished");
                        clearInterval(_self._interval_id);
                        _self.setState({
                            logs: _logs
                        }); 

                        $.ajax({
                            url: _retrieve_console_output,
                            type: "GET",
                            success: function(res){
                                var _log = {
                                    content: res,
                                    type: "console"
                                };
                                
                                _logs.push(_log);
                                _self.setState({
                                    logs: _logs
                                });         
                            },
                            fail: function(res){
                                console.error(res);
                            }
                        });

                    } else {
                        // console.log("Still running.....");

                        // Request again for log
                        $.ajax({
                            url: _retrieve_log_url,
                            type:"GET",
                            success: function(res){
                                var lastLog = _logs.pop();

                                lastLog.content = res;

                                _logs.push(lastLog);
                                
                                _self.setState({
                                    logs: _logs
                                });         
                            },
                            fail: function(res){
                                console.log("failure");
                            }
                        });

                        // _logs.push("Still running.....");
                        
                    }
                },
                done: function(res){
                    console.log("done");
                    console.log(res);
                }
            });
        }, 2000);
    },
    resetStatus:function(e){
        if(this._interval_id!==-1){
            clearInterval(this._interval_id);
        }
        this.props.onMonitorClose();

    },
    handleEnvSelection: function(e){
        console.log("selected");
    },
    render:function() {
    	var logs = this.state.logs.map(function(log){
            if((typeof log) === "string"){
                return (
                    <p>{log}</p>
                );
            } else {
                return (
                    <textarea style={{"width":"100%", "height":"300px"}} readOnly value={log.content}></textarea>
                );
            }
    	});

        var envs = [
            {value:"local_jenkins",text:"local jenkins"},
            {value:"local_environment", text:"local environment"},
            {value:"jenkins_trunk",text:"jenkins trunk"}];


        return (
            <div className="panel panel-primary affix" style={{"width":"40%"}}>
                <div className="panel-heading">
                    <button onClick={this.resetStatus} className="btn btn-xs btn-default pull-right"><span className="glyphicon glyphicon-remove"></span></button>
                    <h5>Execution status</h5>
                </div>
                <div className="panel-body">
                    <fieldset>
                        <legend>Execute configuration</legend>
                        <div className="form-horizontal">
                      <div className="form-group">
                        <label className="col-sm-2 control-label">Execution on: </label>
                        <div className="col-sm-10">
                          <Select2Component id="execution_env_select" styleWidth="100%" placeholder="select execution environment"
                            onSelection={this.handleEnvSelection} dataSet={envs} ></Select2Component>
                        </div>
                      </div>
                    </div>
                    </fieldset>
            	    <fieldset>
                        <legend>Execution Log</legend>
                        <div> {logs}</div>
                    </fieldset>

                </div>
            </div>
        );
    }
});

// module.exports = FeatureExecutionMonitor;

// ReactDOM.render(
//     React.createElement(FeatureExecutionMonitor, null),
//     document.getElementById('feature-execution-log')
// );  
