$(document).ready(function(){
	console.log("page ready");
	$("#create-feature-btn").click(function(e){
		var url = window.location.protocol+"//"+window.location.host+"/auto/feature/create";
		window.location = url;
	})

});
