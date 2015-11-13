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
            featureId: feature_id,
            featureDto: _featureDto
        };
    },
    render: function() {
        return (
            <div>
            	<div className="jumbotron">
					<div className="container">
						<div className="row">
							<FeatureContainer data={this.state.featureDto} />
						</div>
					</div>
            	</div>

            	<ScenarioList data={this.state.featureDto.scenarios} />
            	
            </div>
        );
    }
});

ReactDOM.render(
    React.createElement(FeatureDisplayView, null),
    document.getElementById('feature-info-container')
);  

// module.exports = FeatureDisplayView;