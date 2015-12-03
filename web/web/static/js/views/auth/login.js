$(document).ready(function($){
	"use strict";

	$("#login-button").click(function(e) {
  		
  		$.ajax({
  			url:"/auto/accounts/auth/"+window.location.search,
  			// type:"POST",
  			data:{
  				'csrfmiddlewaretoken': $("#login-form>input")[0].value,
  				'username': $('#lg_username')[0].value,
  				'password': $('#lg_password')[0].value
  			},
  			success: function(res){
  				console.log("success");
  				console.log(res);
  				window.location = res
  			},
  			fail: function(res){
  				console.log("fail");
  				console.log(res);
  				$.growl.error({
  					"title":"valification error!",
  					"message": "Invalid credential, please check"
  				})
  			}
  		})
  	});
});