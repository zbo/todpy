var TOD = TOD || {};
TOD.service = TOD.service || {};

TOD.service.scenarioService = function(){
	function saveScenarioSteps(scenario){

	}

	function parseReactScenarioContainer(react_scenario){
		var dto = {};

		dto.scenario_name = react_scenario.name;
		dto.scenario_id = react_scenario.id;

		dto.steps = react_scenario.steps.map(function(_step){
			var _id = _step.id;
			if(!_id){
				_id="new";
			}
			var result = {};
			delete _step.step.element;
			result[_id] = _step.step;
			result[_id].action_type = _step.type;
			
			return result;
		});

		return dto;
	}


	return {
		"parseScenario": parseReactScenarioContainer
	};
}