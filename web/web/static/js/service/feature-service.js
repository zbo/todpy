var TOD = TOD || {};
TOD.service = TOD.service || {};
TOD.service.featureService = function(){

	var scenarioService = TOD.service.scenarioService();

	function growlSuccess(title, message){
		$.growl.notice({
			"title": title,
			"message": message
		});
	}

	function growlError(title, message){
		$.growl.error({
			"title": title,
			"message": message
		});
	}

	function getFeatureById(feature_id){
		var feature = {};
		try{

			$.ajax({
				type:"GET",
				url: "auto/api/feature/"+feature_id+"/",
				async: false,
				success: function(res){
					feature = res;
				},
				error: function(res){
					console.log("ERROR!!!");
					growlError("ERROR!!!!", "Feature Not Exist");
					throw new Error("Feature Not Exist");
				}
			});	
		} catch (e){
			throw e;
		}
		
		return feature;
	}

	function getFeatureListByPlatform(platform){

	}

	function getFeatureList(){
		var featureList = [];
		$.ajax({
			type: "GET",
			url: "auto/api/feature/list",
			async: false,
			success: function(req, res){
				console.log("Request success");
				featureList = req;
			},
			fail: function(req, res){
				growlError("ERROR!!!!", "Some error occured");
				throw new Error("Feature List error");
			}
		});
		return featureList;
	}

	function saveFeature(feature){
		console.log("create Feature");
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
				growlSuccess("Congratulations", "Feature save success!");
			},
			fail: function(res){
				console.log("fail");
				console.log(res);
				growlError("ERROR!!!!", "Feature save failed");
				throw new Error("Feature Not Saved");
			}
		});
	}

	function updateFeature(feature, feature_id){
		console.log("save Feature");
		var _data = { "feature": feature};
		console.log(JSON.stringify(_data));

		$.ajax({
			type: "POST",
			url: "/auto/update_feature/"+feature_id+"/",
			processData: false,
			data: JSON.stringify(_data),
			success: function(res){
				console.log("success");
				console.log(res);
				growlSuccess("Congratulations", "Feature save success!");
			},
			fail: function(res){
				console.log("fail");
				console.log(res);
				growlError("ERROR!!!!", "Feature save failed");
				throw new Error("Feature Not Saved");
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
		"saveFeature": saveFeature,
		"updateFeature": updateFeature
	};
}