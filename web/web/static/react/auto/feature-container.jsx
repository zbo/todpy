// var React = require('react');

var TOD = TOD || {};
TOD.react = TOD.react || {};

var FeatureContainer = React.createClass({
    displayName: 'FeatureContainer',
    getInitialState: function() {
        return {
        	mode: "display",
        	feature_id: "new",
        	feature_name: "111",
        	feature_description: "1111"
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
        function undefinedOrEmpty(s){
            if( undefined===s || ""===s){
                return true;
            }
            return false;
        }

        if( undefinedOrEmpty(this.state.newVal.feature_name)
            || undefinedOrEmpty(this.state.newVal.feature_description) ){
            
            $.growl.error({
                "title": "Content Error",
                "message": "Feature name cannot be empty"
            });

        } else {
            this.setState({
                mode: "display",
                feature_name: this.state.newVal.feature_name,
                feature_description: this.state.newVal.feature_description
            });             
        }

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

        console.log(this.props);
        if(this.props.data){
            var _mode = this.props.data.mode? this.props.data.mode: "display";
            console.log(_mode);
            this.setState({
                mode: _mode,
                feature_id: this.props.data.feature_id,
                feature_name: this.props.data.name,
                feature_description: this.props.data.description,
                newVal: {
                    feature_id: this.props.data.feature_id,
                    feature_name: this.props.data.name,
                    feature_description: this.props.data.description
                }
            });
        }
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
                    <h4>Edit Feature information</h4>
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
		            <p id="feature_description" style={{"overflow": "auto","wordWrap": "break-word"}}>{this.state.feature_description}</p>
		        </div>
	        );
    	}
        
    }
});

TOD.react.FeatureContainer = FeatureContainer;

// module.exports = FeatureContainer;

if(document.getElementById('feature-container')){
    console.log("execute")
    ReactDOM.render(
       React.createElement(FeatureContainer, null),
       document.getElementById('feature-container')
    );    
}
