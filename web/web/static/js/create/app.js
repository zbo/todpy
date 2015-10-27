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