$("#create_scenario").click(function(){
    appendScenarioForm($("#scenarios-container"));
});

function appendScenarioForm(domElement){
     var container = '<div class="panel panel-default">'
          +'<div class="panel-heading">'
                    +'<h3 class="panel-title">Scenario</h3>'
                +'</div>'
                +'<div class="panel-body">'
                    +'Panel content'
                +'</div>'
            +'</div>';
       domElement.append(container);

}

var TOD = TOD || {};
TOD.btn = {};

$(document).ready(function(){
    $(".step-edit-btn").click(function(e){
      TOD.btn = e.target;
      console.log(TOD.btn)
      var step_container = $(TOD.btn.parentElement.previousElementSibling);
      TOD.selectedType = step_container.find("span.step-type")[0].dataset["type"];
      TOD.selectedStep = step_container.find("span.step-description")[0].innerHTML;


    });

    $("select").select2();
});