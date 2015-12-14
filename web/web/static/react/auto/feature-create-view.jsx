// var React = require('react');

var FeatureCreateView = React.createClass({
    displayName: 'FeatureCreateView',
    getInitialState:function() {
        return {
            featureInfo: {
            	mode:"edit",
            	feature_id:"new",
            	feature_name:"",
            	feature_description:""
            },
            scenarios: []
        };
    },
    componentWillMount:function() {

    },
    saveFeature: function(){
    	PubSub.publish(TOD.events.getFeatureData);
        PubSub.publish(TOD.events.getScenarioData);

        var featureData = TOD.react.data.feature,
            scenarioData = TOD.react.data.scenarios;

       	var featureService = new TOD.service.featureService();

        if(featureService.parseFeatureDto(featureData, scenarioData)){
       		featureService.saveFeature(featureData);
       	} else {
       		$.growl.error({
       			"title": "Validation Error!",
       			"message" : "The data is invalid"
       		})
       	}

    },
    addScenario: function(){
    	var new_scenario = {
    		mode: "edit",
    		id: "new",
    		name: "",
    		description: "",
    		steps: []
    	};

    	var _scenarios = this.state.scenarios;
    	_scenarios.push(new_scenario);
    	this.setState({
    		scenarios: _scenarios
    	});

    },
    backToList: function(){
    	var url = window.location.protocol+"//"+window.location.host+"/auto/features/";
    	window.location = url;
    },
    render: function() {
    	var _self = this;
        return (
             <div>
                <div className="page-header" style={{"textAlign":"right"}}>
                    <button onClick={this.saveFeature} id="btn_save_feature" className="btn btn-success">Save</button>
                    <button onClick={this.addScenario} id="btn_create_feature" className="btn btn-primary">Create Scenario</button>
                    <button onClick={this.backToList} id="btn_back_feature" className="btn btn-default">Back</button>
                </div>
                <div className="row">
   					<div className="col-md-12">
                        <div className="well wel-sm">
                           <div className="row">
                                <FeatureContainer data={_self.state.featureInfo} />
                            </div>
                        </div>
                        <fieldset>
                        	<legend>Scenarios</legend>
                       		<ScenarioList data={_self.state.scenarios} />
                       	</fieldset>
                    </div>
                </div>
            </div>
        );
    }
});



// module.exports = FeatureCreateView;
