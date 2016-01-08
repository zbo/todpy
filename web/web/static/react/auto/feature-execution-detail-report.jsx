// var React = require('react');

var FeatureExecutionReport = React.createClass({
    displayName: 'FeatureExecutionReport',
    getInitialState() {
        return {
        	featureId : -1,
            errorScreenShots: {},
            activeTab: 1,
            result: {
            	passes: 0,
            	errors: 0,
            	failures: 0,
            	tests: 0
            },
            detail_result: {},
            showScreenshot: false,
            selectedStep: {
            	name: "",
            	path: ""
            },
            screenshots:[]
        };
    },
    componentWillMount:function() {
    	var _self = this;
    	$.ajax({
    		url: "/workspace/api/read_screenshot_index/"+this.props.featureId+"/",
    		async: false,
    		success: function(res){
    			var xml = (new DOMParser()).parseFromString(res,"text/xml");
    			_self.state.detail_result = xmlToJson(xml);
    			console.log(_self.state.detail_result);
    		}
    	})

        this.setState({
        	featureId: this.props.featureId,
       		result: this.props.data
       	})
    },
    handleSelect: function(key){
    	console.log(key);
    	this.setState({
    		activeTab: key
    	})
    },
    openScreenShot: function(pathTo){
    	var _pathTo = pathTo.target.dataset['image'],
    		stepName = pathTo.target.innerHTML;
    	var _self = this;

    	if(this.state.screenshots[_pathTo]){
    		//The screenshots is cached locally
    		_self.setState({
			  	showScreenshot:true,
			  	selectedStep: {
			  			name:stepName,
			  			path: _pathTo
			  		}
			});
    	} else {
    		// get the screenshots from server
    		// then pop up a dialog or overlay to demonstrate it
    		

    		$.ajax({
			  url:window.location.protocol+"//"+window.location.host+"/workspace/api/read_screenshot_by_path",
			  type: "POST",
			  processData: false,
			  data:JSON.stringify({
			    path: _pathTo,
			    featureId: _self.state.featureId,
			    'csrfmiddlewaretoken': $("#csrf_crendential>input")[0].value
			  }),
			  success: function(res){
			  	var _screenshots = _self.state.screenshots;
			  	_screenshots[_pathTo] = "data:image/png;base64,"+res;
			  	
			  	_self.setState({
			  		showScreenshot:true,
			  		selectedStep: {
			  			name:stepName,
			  			path: _pathTo
			  		},
			  		screenshots: _screenshots
			  	})
			  },
			  fail: function(res){
			  	console.log(res);
			  }
			})
    	}
    },
    closeDetailModal: function(){
    	this.setState({
    		showScreenshot:false,
    		selectedStep: {
    			name:"",
    			path:""
    		}
    	});
    },
    render:function() {
    	var screenshot;
    	var _self = this;

    	var screenshot_index = (function(){
    		var result = _self.state.detail_result;
    		var feature = result.feature,
    			scenarios = feature.scenario;

    		var $scenarios = scenarios.map(function(scenario){
    			var steps = scenario.step.map(function(_step){
    				var s = _step['@attributes'];
    				var pass = JSON.parse(s.pass);
    				var path = pass? scenario['@attributes'].path+"/"+s.img: scenario['@attributes'].path+"/error.png",
    					_class = pass? "bg-success": "bg-danger";

    				return (
    					<p className={_class} >
    						<a data-image={path} onClick={_self.openScreenShot}>{s.name}</a>
    					</p>
    				);
    			});

    			return (
    				<div className="panel panel-primary">
	    				<div className="panel-heading" data-path={scenario['@attributes'].path}>
	    					{scenario['@attributes'].name}
	    				</div>
	    				<div className="panel-body">
	    					{steps}
	    				</div>
    				</div>
    			);
    		});

    		return $scenarios;
    	})();

    	var screenshotDialog = !_self.state.showScreenshot?"":(function(){
    		var imgData = _self.state.screenshots[_self.state.selectedStep.path];
    		return (
                <ReactBootstrap.Modal show={_self.state.showScreenshot} onHide={_self.closeDetailModal}>
                  <ReactBootstrap.Modal.Header closeButton>
                    <ReactBootstrap.Modal.Title>{_self.state.selectedStep.name}</ReactBootstrap.Modal.Title>
                  </ReactBootstrap.Modal.Header>
                  <ReactBootstrap.Modal.Body>
                    <img src={imgData} style={{"width":"100%", "overflow":"auto"}}></img>
                  </ReactBootstrap.Modal.Body>
                  
                </ReactBootstrap.Modal>
    		);
    	})();

        return (
            <div>
            	<div style={{"display":"inline-block"}}>
	                <span className="label label-primary">total: {this.state.result.tests}</span>
	                <span className="label label-success">pass: {this.state.result.passes}</span>
	                <span className="label label-warning">errors: {this.state.result.errors}</span>
	                <span className="label label-danger">failures: {this.state.result.failures}</span>
	            </div>
	           	<ReactBootstrap.Tabs activeKey={this.state.activeTab} onSelect={this.handleSelect}>
   	                <ReactBootstrap.Tab eventKey={1} title="Step Screenshot">
	                	{screenshot_index}
	                </ReactBootstrap.Tab>
	                <ReactBootstrap.Tab eventKey={2} title="Error Screenshot">
	                </ReactBootstrap.Tab>
	            </ReactBootstrap.Tabs>
	            {screenshotDialog}
            </div>
        );
    }
});

// module.exports = FeatureExecutionReport;