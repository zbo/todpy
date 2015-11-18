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
    	PubSub.subscribe(TOD.events.runFeature, this.pollForUpdate); 
    },
    pollForUpdate: function(){
    	// poll the server for execution log
    	var _url = window.location.protocol+"//"+window.location.host+"/auto/feature/exe/"+this.state.featureId+"/";
    	var _self = this;
    	var interval_id = setInterval(function(){
    		$.ajax({
	    		url:_url,
	    		type:"GET",
	    		success: function(res){
	    			console.log("success");
	    			if("result:execution already started"===res){
	    				alert(res);
	    				window.clearInterval(interval_id);
	    				return ;
	    			}
	    			var _logs = _self.state.logs;

	    			_logs.push(res);
	    			_self.setState({
	    				logs: _logs
	    			});
	    		},
	    		done: function(res){
	    			console.log("done");
	    			console.log(res);
	    		}
	    	})
    	}, 2000);
    	
    },
    render:function() {
    	var logs = this.state.logs.map(function(log){
    		return (
    			<p>{log}</p>
    		)
    	});
        return (
            <div >
            	{logs}
            </div>
        );
    }
});

// module.exports = FeatureExecutionMonitor;

ReactDOM.render(
    React.createElement(FeatureExecutionMonitor, null),
    document.getElementById('feature-execution-log')
);  
