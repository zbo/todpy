// var React = require('react');

var ScenariosContainer = React.createClass({
    displayName: 'ScenariosContainer',
    getInitialState() {
        return {
            scenarios: []
        };
    },
    render: function() {
    	var stepList = this.state.steps.map(function(step){
    		return <li data={step} >{this.state.name}</li>
    	});

        return (
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title" style="display: inline-block;">Scenario</h3>
                    <button class="btn btn-sm btn-default" style="right: 24px;position: absolute;">
                        <span class="glyphicon glyphicon-minus"></span>
                    </button>
                </div>
                <div class="panel-body">
                    <div class="btn-group" role="group" style="display:flex; margin-bottom: 5px" >
                           <button onClick={this.onAddButtonClick} name="add-step" type="button" class="btn btn-default">Add Step</button>
                    </div>


                </div>
            </div>
        );
    }
});

// export var ScenarioContainer;
// module.exports = ScenarioContainer;