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
    	var scenarioComponents = this.state.scenarios.map(function(scenario){
    		return (
    			<ScenarioContainer key={scenario.id} data={scenario}/>
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