// var React = require('react');

var FeatureDisplayView = React.createClass({
    displayName: 'FeatureDisplayView',
    getInitialState: function() {
    	var featureService = new TOD.service.featureService();

		var feature_id = $("#feature-page-header")[0].dataset['featureId'];
		try{
			_featureDto = featureService.getFeatureById(feature_id);
			_featureDto.feature_id=feature_id;
			console.log(_featureDto);
		} catch (e){
			throw e;
		}

        return {
            mode:"display",
            featureId: feature_id,
            featureDto: _featureDto
        };
    },
    viewRemote: function(e){
        window.open('http://10.32.36.71:6080/vnc_auto.html')
    },
    runFeature: function(e){
        console.log("start running");
        this.setState({
            mode:"executing"
        });
        PubSub.publish(TOD.events.runFeature);
    },
    saveFeature: function(e){
        console.log("save feature");
        PubSub.publish(TOD.events.getFeatureData);
        PubSub.publish(TOD.events.getScenarioData);

        var featureData = TOD.react.data.feature,
            scenarioData = TOD.react.data.scenarios;

        var featureService = new TOD.service.featureService();
        featureService.parseFeatureDto(featureData, scenarioData);

        featureService.updateFeature(featureData, this.state.featureId);
    },
    addScenario: function(){
        var new_scenario = {
            id: "new",
            name: "",
            description: "",
            steps: []
        };

        var _scenarios = this.state.featureDto.scenarios;
        _scenarios.push(new_scenario);
        this.setState({
            featureDto: this.state.featureDto
        });

    },
    closeMonitor: function(e){
        this.setState({
            mode:"display"
        });
    },
    backToList: function(){
        var url = window.location.protocol+"//"+window.location.host+"/auto/features/";
        window.location = url;
    },
    render: function() {
        var _self = this;
        var view = (function(){
            if("display" === _self.state.mode){
                return (
                <div className="row">

                    <div className="col-md-12">
                        <div className="well wel-sm">
                           <div className="row">
                                <FeatureContainer data={_self.state.featureDto} />
                            </div>
                        </div>
                        <fieldset>
                            <legend>Scenarios</legend>
                            <ScenarioList data={_self.state.featureDto.scenarios} />
                        </fieldset>
                   </div>
                </div>
                );
            } else {
                return (
                <div className="row">
                    <div className="col-md-6">
                        <div className="well wel-sm">
                           <div className="row">
                                <FeatureContainer data={_self.state.featureDto} />
                            </div>
                        </div>
                        <fieldset>
                            <legend>Scenarios</legend>
                            <ScenarioList data={_self.state.featureDto.scenarios} />
                        </fieldset>
                   </div>
                   <div className="col-md-6">
                        <FeatureExecutionMonitor onMonitorClose={_self.closeMonitor}/>
                   </div>
                </div>
                );
            }
        })();

        var buttonGroup=(function(){
            if("display" === _self.state.mode){
                return (
                    <div className="page-header" style={{"textAlign":"right"}}>
                        <button onClick={_self.saveFeature} id="btn_save_feature" className="btn btn-success">Save</button>
                        <button onClick={_self.runFeature} id="btn_exe_feature" className="btn btn-warning">Execute</button>
                        <button onClick={_self.addScenario} id="btn_add_scenario" className="btn btn-primary">Add scenraio</button>
                        <button onClick={_self.backToList} id="btn_back_feature" className="btn btn-default">Back</button>
                    </div>
                );

            } else {
                return (
                    <div className="page-header" style={{"textAlign":"right"}}>
                        <button onClick={_self.viewRemote} id="btn_view_remote" className="btn btn-success">View Remote</button>
                        <button onClick={_self.runFeature} id="btn_run_feature" className="btn btn-warning">Run</button>
                        <button onClick={_self.runFeature} id="btn_debug_feature" className="btn btn-primary">Debug</button>
                        <button onClick={_self.closeMonitor} id="btn_edit_feature" className="btn btn-default">Edit Feature</button>
                    </div>
                );
            }

        })();

        return (
            <div>
                {buttonGroup}
                {view}
            </div>
        );
    }
});

ReactDOM.render(
    React.createElement(FeatureDisplayView, null),
    document.getElementById('feature-info-container')
);

// module.exports = FeatureDisplayView;
