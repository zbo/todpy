var TOD = TOD || {};
TOD.service = TOD.service || {};

TOD.service.StepService = function(){

	function getAllDefinedSteps(){

	}

	function getDefinedStepsByPlatform(platform){
		
		var dataObj;
		$.ajax({
			url: "/auto/search_steps?type="+platform,
			async: false 
		}).fail(function(res){
			console.log("fail");
		}).success(function(res){
			dataObj = res;
		});

		var dataArray = [];
		var _id = 0;

		for(var index in dataObj){
			if(dataObj[index]){
				var step = dataObj[index];
				step.id = _id++;
				step.value = index;
				step.text = index;
				TOD.util.stepParser.decorateDescriptionPlaceHolder(step);
				dataArray.push(step);
			}			
		}

		return dataArray;
	}

	function getDefinedStepsByPlatformAndType(platform, type){

	}

	function getDefinedStepsByPlatformWithPagenator(platform, start, length){


	}

	return {
		"getDefinedStepsByPlatform": getDefinedStepsByPlatform
	};
};


TOD.util = TOD.util || {};
TOD.util.stepParser = {
	ANY_STRING: "'([^']*)'",
	ONLY_NUMBER: "(\d+)",
	parseDescription: function(step_Definition){
		var _argCount = step_Definition.co_argcount,
			_varNames = step_Definition.co_varnames,
			_stepText = step_Definition.value,
			_variables = step_Definition.co_variables;

		if(_argCount<=1){
			step_Definition.description = _stepText;
		}
		else {
			for(var i=1;i<argCount;i++){
				//Should traverse the String and replace all placeholder with val from _variables
				var replacement = _variables[_varNames[i]];


				var _indexAnyString = _stepText.indexOf(this.ANY_STRING),
					_indexOnlyNumber = _stepText.indexOf(this.ONLY_NUMBER);

				// If _indexAnystring equal to _indexOnlyNumber
				// then it must be below 0

				if ((_indexOnlyNumber>=0) && (_indexAnyString>_indexOnlyNumber || _indexAnyString<0)){
					_stepText = _stepText.replace(this.ONLY_NUMBER, replacement);

				} else if((_indexAnyString>=0) && (_indexAnyString<_indexOnlyNumber|| _indexOnlyNumber<0)){
					_stepText = _stepText.replace(this.ANY_STRING, replacement);
				}
			}

			step_Definition.description = _stepText;
		}
	},
	decorateDescriptionPlaceHolder: function(step_Definition){
		if(!step_Definition){
			return ;
		}
		var _stepText = step_Definition.text;
		var _indexAnyString = _stepText.indexOf(this.ANY_STRING),
			_indexOnlyNumber = _stepText.indexOf(this.ONLY_NUMBER);

		while(_indexOnlyNumber>=0 || _indexAnyString>=0){
			if(_indexAnyString>=0){
				_stepText = _stepText.replace(this.ANY_STRING, "'[?]'");
			}

			if(_indexOnlyNumber>=0){
				_stepText = _stepText.replace(this.ONLY_NUMBER, "'[?#]'")
			}
			_indexAnyString = _stepText.indexOf(this.ANY_STRING);
			_indexOnlyNumber = _stepText.indexOf(this.ONLY_NUMBER);
		}

		step_Definition.text = _stepText;
	}
};






























