// var React = require('react');

var FeatureExecutionHistory = React.createClass({
    displayName: 'FeatureExecutionHistory',
    getInitialState:function() {
        return {
        	history:[]
        };
    },
    componentWillMount:function() {
    	var _self = this,
    		_url = window.location.protocol+"//"+window.location.host+"/workspace/api/read_build_history/"+this.props.data.featureId;

    	$.ajax({
    		url: _url,
    		success: function(res){
    			var _history = JSON.parse(res);
    			console.log("success")
    			_self.setState({
    				history:_history
    			})
    		}, 
    		fail: function(res){
    			//Todo handle failure 
    		}
    	})
    	
    },
    render:function() {
    	var _history = this.state.history;

    	var $dom = _history.map(function(record){
    		var _pass = parseInt(record['pass']),
    			_failure = parseInt(record['failure']),
    			_error = parseInt(record['error']),
    			_total = parseInt(record['total']),
    			_id = record['id'],
    			_directory = record['directory']

    		var _class = (_total===_pass)? "list-group-item list-group-item-success": "list-group-item list-group-item-danger";

    		return (
    			<a href="#" className={_class} key={_id}>
    				<label>BUILD #</label>
    				<span style={{"marginRight":"10px"}}>{_id}</span>
    				<span className="label label-success">pass: {_pass}</span>
    				<span className="label label-danger">failure: {_failure}</span>
    				<span className="label label-warning">error: {_error}</span>
    				<span className="label label-info">total: {_total}</span>
    				<span> time:</span>TBD
    			</a>
    		);
    	});

        return (
            <div className="list-group">
			  {$dom}
			</div>
        );
    }
});

// module.exports = FeatureExecutionHistory;