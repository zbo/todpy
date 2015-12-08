// var React = require('react');

var ScenarioList = React.createClass({
    displayName: 'ScenarioList',
    getInitialState:function() {
        return {
            scenarios: []  
        };
    },
    componentDidMount() {
        if(this.props.data){
        	this.setState({
                scenarios: this.props.data
        	});
        } 
    },
    render: function() {
        var index = 0;

    	var scenarioComponents = this.state.scenarios.map(function(scenario){
            var _key = "scenario:" + (index++);
    		return (
    			<ScenarioContainer key={_key} react_key={_key} data={scenario}/>
    		);
    	});

        return (
            <div className="scenario-list">
            	{ scenarioComponents }
            </div>
        );
    }
});

// module.exports = ScenarioList;