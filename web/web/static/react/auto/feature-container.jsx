// var React = require('react');

var FeatureContainer = React.createClass({
    displayName: 'FeatureContainer',
    getInitialState: function() {
        return {
        	mode: "display",
        	feature_id: "new",
        	feature_name: "Update apps order in App Gallery",
        	feature_description: "As a Product manager I want to re-order the public apps so that RC apps come first, then followed by 3rd party apps and coming soon apps."
        };
    },
    getFeatureData: function(){
		TOD.react.data.feature = this.state;
    },
    editButtonClicked: function(e){
    	// Enter edit mode
    	this.setState({
    		mode: "edit",
            newVal: {
                feature_id: this.state.feature_id,
                feature_name: this.state.feature_name,
                feature_description: this.state.feature_description
            }
    	});
    },
    saveButtonClicked: function(e){

        this.setState({
    		mode: "display",
            feature_name: this.state.newVal.feature_name,
            feature_description: this.state.newVal.feature_description
    	});	
    },
    cancelButtonClicked: function (e){
    	this.setState({
    		mode: "display"
    	});
    },
    handleValueChange: function(e){
        var _index = e.target.dataset['name'];
        _newVal = e.target.value;
        var _attr = this.state.newVal;
        _attr[_index] = _newVal;
        this.setState({
            newVal: _attr
        });
    },
    componentWillMount:function() {
        PubSub.subscribe(TOD.events.getFeatureData, this.getFeatureData);
        return true;
    },
    render: function() {
        
    	if("edit"===this.state.mode){
    		var _name = this.state.newVal.feature_name,
    			_description = this.state.newVal.feature_description;
    		return (
    			<div id="feature-info-panel" className="col-sm-12">
		        	<div className="pull-right btn-group">
		        		<button onClick={this.saveButtonClicked} className="btn btn-primary btn-xs"><span className="glyphicon glyphicon-floppy-save"/>Save</button>
		        		<button onClick={this.cancelButtonClicked} className="btn btn-danger btn-xs"><span className="glyphicon glyphicon-remove"/>Cancel</button>
		        	</div>
		            <div className="form-horizontal" style={{"marginTop":"30px"}}>
                      <div className="form-group">
                        <label className="col-sm-2 control-label">Feature: </label>
                        <div className="col-sm-10">
                          <input onChange={this.handleValueChange} data-name="feature_name" type="text" className="form-control" value={_name}></input>
                        </div>
                      </div>
                      <div className="form-group">
                        <label className="col-sm-2 control-label">Description: </label>
                        <div className="col-sm-10">
                          <input onChange={this.handleValueChange} data-name="feature_description" type="text" className="form-control" value={_description}></input>
                        </div>
                      </div>
                    </div>
		            
		        </div>
    		);
    	} else {
    		return (
		        <div id="feature-info-panel" className="col-sm-12">
		        	<div className="pull-right btn-group">
		        		<button onClick={this.editButtonClicked} className="btn btn-default btn-xs"><span className="glyphicon glyphicon-edit"/>Edit</button>
		        	</div>
		            <h3>Feature Name: {this.state.feature_name}</h3>
		            <p id="feature_description">{this.state.feature_description}</p>
		        </div>
	        );
    	}
        
    }
});

// module.exports = FeatureContainer;
ReactDOM.render(
   React.createElement(FeatureContainer, null),
   document.getElementById('feature-container')
);