var TOD = TOD || {};
TOD.service = TOD.service || {};

TOD.service.testPlanService = function(){
    function getAllTestPlans(){
      var dataObj;
      $.ajax({
  			url: "/auto/api/testplan/list",
  			type: "GET",
  			async: false,
  			data: {
  			}
  		}).fail(function(res){
  			console.log("fail");
  		}).success(function(res){
  			dataObj = res;
  		});
      return dataObj;
    };

    return {
  		"getAllTestPlans": getAllTestPlans
  	};
}
