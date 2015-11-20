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
    closeMonitor: function(e){
        this.setState({
            mode:"display"
        });
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
                       <ScenarioList data={_self.state.featureDto.scenarios} />
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
                       <ScenarioList data={_self.state.featureDto.scenarios} />
                   </div>
                   <div className="col-md-6">
                        <FeatureExecutionMonitor onMonitorClose={_self.closeMonitor}/>
                   </div>
                </div>
                );
            }
        })();

        return (
            <div>
                <div className="page-header" style={{"textAlign":"right"}}>
                    <button onClick={this.saveFeature} className="btn btn-success">Save</button>
                    <button onClick={this.runFeature} className="btn btn-warning">Run</button>
                </div>
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