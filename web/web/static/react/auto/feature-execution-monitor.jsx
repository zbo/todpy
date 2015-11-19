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
    componentWillMount: function() {
    	PubSub.subscribe(TOD.events.runFeature, this.requestForStartExecution); 
    },
    requestForStartExecution:function(){
        var _url = window.location.protocol+"//"+window.location.host+"/auto/feature/exe/"+this.state.featureId+"/";
        var _self = this;
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
                    _logs.push("==============================");
                    _logs.push("Execution Started");
                    _self.state.s_time = 
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
    pollForUpdate: function(){
    	// poll the server for execution log
    	var _url = window.location.protocol+"//"+window.location.host+"/auto/feature/exe-status/"+this.state.featureId+"/";
        var _self = this;
        
        var interval_id = setInterval(function(){
            $.ajax({
                url:_url,
                type:"GET",
                success: function(res){
                    console.log("execution result");
                    console.log(res);
                    var _logs = _self.state.logs;
                    if("locked:False"===res){
                        console.log("Run success");
                        
                        _logs.push("Execution Finished");
                        _logs.push("==============================");

                        _self.setState({
                            logs: _logs
                        }); 
                        clearInterval(interval_id);
                    } else {
                        console.log("Still running.....");
                        _logs.push("Still running.....");
                        _self.setState({
                            logs: _logs
                        }); 
                    }
                },
                done: function(res){
                    console.log("done");
                    console.log(res);
                }
            });
        }, 2000);
        
    },
    render:function() {
    	var logs = this.state.logs.map(function(log){
    		return (
    			<p>{log}</p>
    		)
    	});
        return (
            <div className="panel panel-primary">
                <div className="panel-heading">
                    <button onClick={this.props.onMonitorClose} className="btn btn-xs btn-default pull-right"><span className="glyphicon glyphicon-remove"></span></button>
                    <h4>Execution status</h4>
                </div>
                <div className="panel-body">
            	   {logs}
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
