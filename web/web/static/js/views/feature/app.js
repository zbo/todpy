$(document).ready(function(){
	console.log("page ready");
	$("#create-feature-btn").click(function(e){
		var url = window.location.protocal+"//"+window.location.host+"/auto/create";
		window.location = url;
	})	

});

	