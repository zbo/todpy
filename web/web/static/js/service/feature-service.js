var TOD = TOD || {};
TOD.service = TOD.service || {};
TOD.service.featureService = function(){

	var scenarioService = TOD.service.scenarioService();

	function getFeatureById(feature_id){

	}

	function getFeatureListByPlatform(platform){

	}

	function getFeatureList(){
		var featureList = [];
		$.ajax({
			type: "GET",
			url: "/auto/feature/list",
			async: false,
			success: function(req, res){
				console.log("Request success");
				featureList = req;
			}
		});
		return featureList;
	}

	function saveFeature(feature){
		console.log("saveFeature");
		var _data = { "feature": feature};
		console.log(JSON.stringify(_data));

		$.ajax({
			type: "POST",
			url: "/auto/save_feature",
			processData: false,
			data: JSON.stringify(_data),
			success: function(res){
				console.log("success");
				console.log(res);
			},
			fail: function(res){
				console.log("fail");
				console.log(res);
			}
		});
	}

	function parseFeatureFromReact(feature, scenarios){
		var _scenario_dtos = scenarios.map(function(scenario){
			var _scenario = scenarioService.parseScenario(scenario);
			return _scenario;
		});
		
		feature.scenarios = _scenario_dtos;

	}

	return {
		"getFeatureById": getFeatureById,
		"getFeatureList": getFeatureList,
		"getFeatureListByPlatform": getFeatureListByPlatform,
		"parseFeatureDto": parseFeatureFromReact,
		"saveFeature": saveFeature
	};
}