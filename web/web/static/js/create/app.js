var TOD = TOD || {};


$(document).ready(function(){
    $("#save_feature").click(function(){
        PubSub.publish(TOD.events.getFeatureData);
        PubSub.publish(TOD.events.getScenarioData);
        
        var featureData = TOD.react.data.feature,
            scenarioData = TOD.react.data.scenarios;
        
        var featureService = new TOD.service.featureService();
        featureService.parseFeatureDto(featureData, scenarioData);

        featureService.saveFeature(featureData);
    })
});