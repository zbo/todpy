// var React = require('react');

var FeatureContainer = React.createClass({
    displayName: 'FeatureContainer',
    getInitialState: function() {
        return {
        	feature_id: "new",
        	feature_name: "Update apps order in App Gallery",
        	feature_description: "As a Product manager I want to re-order the public apps so that RC apps come first, then followed by 3rd party apps and coming soon apps."
        };
    },
    getFeatureData: function(){
		TOD.react.data.feature = this.state;
    },
    componentWillMount:function() {
        PubSub.subscribe(TOD.events.getFeatureData, this.getFeatureData);
        return true;
    },
    render: function() {
        return (
        <div id="feature-info-panel" className="col-sm-12">
        	<div className="pull-right btn-group">
        		<button className="btn btn-default btn-xs"><span className="glyphicon glyphicon-edit"/>Edit</button>
        	</div>
            <h3>Feature Name: {this.state.feature_name}</h3>
            <p id="feature_description">{this.state.feature_description}</p>
        </div>
        );
    }
});

// module.exports = FeatureContainer;
ReactDOM.render(
   React.createElement(FeatureContainer, null),
   document.getElementById('feature-container')
);