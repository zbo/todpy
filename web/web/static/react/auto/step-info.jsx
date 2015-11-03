// var React = require('react');
var TOD = TOD || {};
TOD.react = TOD.react || {};

var StepInfoDisplay = React.createClass({
    displayName: 'StepInfoDisplay',
    changeMode: function(e){
        this.props.onChangeMode("edit");
    },
    deleteStep: function(e){
        this.props.onDeleteButtonClick(this.props.data);
    },
    render: function() {
        console.log("React Render")
        var _self = this;
        return (
        <div className="row">
            <div className="col-md-10" >
                <span data-type={this.props.data.type} style={{"fontWeight":"bold","marginRight":"3px"}} className="step-type">{this.props.data.type}</span>
                <span className="step-description">{this.props.data.description}</span>
            </div>
            <div className="col-md-2">
                <button onClick={this.changeMode} data-next="edit"  className="btn btn-xs btn-primary">Edit</button>
                <button onClick={this.deleteStep} className="btn btn-xs btn-danger">X</button>
            </div>
        </div>
        );
    }
});

var StepInfoEdit = React.createClass({
    displayName: 'StepInfoEdit',
    getInitialState: function() {
        console.log("getInitialState");
        var _index = Math.round(10000000*Math.random());
        return {
            index: _index,
            data: {
                id: -1,
                type: "",
                description: "desc1",
                value: {}
            }  
        };
    },
    componentWillMount: function() {

        if(!this.props.data.id){
            this.props.data.id = Math.round(1000000*Math.random());
        }
        console.log(this.props.data);

        this.setState({
            data:{
                id: this.props.data.id,
                type:this.props.data.type,
                description: this.props.data.description
            }
        });
    },
    handleItemChange: function(e){
        var updateProp = e.target.dataset.name;
        console.log(updateProp);
        
        this.state.data[updateProp] = e.target.value;
        this.setState({
          "data": this.state.data
        });
    },
    handleTypeSelections: function(e, selections){
        this.setState({
            data: {
                id: this.state.data.id,
                type: selections[0].value,
                description: this.state.data.description
            }
        });
    },
    handleStepSelections: function(e, selections){
        console.log(selections);
        this.setState({
            data: {
                id: this.state.data.id,
                type: this.state.data.type,
                description: selections[0].text
            }
        });
    },
    saveChange: function(e){
        this.props.onContentChange(this.state.data);
        this.props.onChangeMode("display");
    },
    discardChange: function(e){
        this.props.onChangeMode("display");  
    },
    render: function() {
        var type = this.state.data.type;
        var description = this.state.data.description;
        var supportedType = [
            {id: 0, text: "Given", value: "Given"},
            {id: 1, text: "When", value: "When"},
            {id: 2, text: "Then", value: "Then"}
        ];

        var stepService = new TOD.service.StepService();
        var providedSteps = stepService.getDefinedStepsByPlatform("web");

        var typeIndex = [supportedType.findIndex(function(e){
            return e.text===type;
        })];

        var selectTypeId = "select-step-type-"+this.state.id;
        var selectStepId = "select-step-"+this.state.id;

        var parameterList = (function(){
            return (
                <div className="parameter_list" style={{"marginTop":"5px"}}>
                    <form className="form-horizontal">
                      <div className="form-group">
                        <label for="inputEmail3" className="col-sm-2 control-label">Arg1: </label>
                        <div className="col-sm-10">
                          <input type="textarea" className="form-control" ></input>
                        </div>
                      </div>
                    </form>
                </div>
            );
        })();

        return (
        <div className="row">
            <div className="col-md-10">
                <div className="row">
                    <div className="col-sm-3">
                        <h4>By Type</h4>
                        <Select2Component id={selectTypeId}
                            styleWidth="100%"
                            placeholder="select type"
                            onSelection = {this.handleTypeSelections}
                            dataSet={supportedType}
                            val={[1]}
                            data-name="type"/>
                    </div>
                    <div className="col-sm-9">
                        <h4>Select Step</h4>
                        <Select2Component id={selectStepId}
                            styleWidth="100%"
                            placeholder="select step"
                            onSelection = {this.handleStepSelections}
                            dataSet={providedSteps}
                            val={[1]}
                            data-name="description"/>
                    </div>
                </div>
                <div className="row" style={{"borderTop":"1px dashed gray","marginTop":"5px"}}>
                    <div className="col-sm-12">
                        {parameterList}
                    </div>
                </div>
            </div>
            <div className="col-md-2" style={{"marginTop":"20px"}}>
                <button onClick={this.saveChange} data-next="display" className="btn btn-xs btn-success">Save</button>
                <button onClick={this.discardChange} data-next="display" className="btn btn-xs btn-danger">X</button>
            </div>            
        </div>
        );
    }
});


TOD.react.StepInfo = React.createClass({
    displayName: 'StepInfo',
    getInitialState: function() {
        return {
            mode: "display",
            data: {
                id: -1,
                type: "Given",
                description: "This is description from React",
                step: {}
            }
        };
    },
    componentWillMount: function(){
        this.setState({
            mode: this.props.data.mode,
            data: {                id: this.props.data.id,
                type: this.props.data.type,
                description: this.props.data.description
            }
        });
    },
    changeMode: function(next_state){
        this.setState({mode:next_state});
    },
    handleContentChange: function(_data){
        console.log("handleContentChange");
        console.log(_data);
        this.setState({
            mode: "display",
            data:{
                id: _data.id,
                type: _data.type,
                description: _data.description
            }
        });
        this.props.onContentChange(_data);
    },
    render: function() {
        // console.log("React Render")
        var _self = this;
        var component = (function(){
            switch (_self.state.mode)
            {
                case "display":
                    return (<StepInfoDisplay key={_self.state.data.id} onChangeMode={_self.changeMode} onDeleteButtonClick={_self.props.onDeleteButtonClick} data={_self.state.data}/>);
                case "edit":
                    return (<StepInfoEdit key={_self.state.data.id} onContentChange={_self.handleContentChange} onChangeMode={_self.changeMode} data={_self.state.data}/>);
            }
        })();

        return (
            <div className="well well-sm">
                {component}
            </div>
        );
    }
});


TOD.react.ScenarioContainer = React.createClass({
    displayName: 'ScenarioContainer',
    getInitialState() {
        return {
            name: "name of scenario",
            description: "description of scenario",
            steps: [
                {
                    id: 1,
                    mode: "display",
                    type: "Given",
                    description: " a clean and valid account in system"，
                    step: {

                    }
                },
                {
                    id: 2,
                    mode: "display",
                    type: "When",
                    description: "2. I login the system"
                },
                {
                    id: 3,
                    mode: "display",
                    type: "Then",
                    description: "3. I have authorization of developer"
                },
                {
                    id: 4,
                    mode: "display",
                    type: "When",
                    description: "4. I try to access NPA functionanlirty"
                },
                {
                    id: 5,
                    mode: "display",
                    type: "Then",
                    description: "5. I can see what I wanted to see"
                }
            ]
        };
    },
    componentWillUpdate(nextProps, nextState) {
          
        return true;
    },
    onAddButtonClick: function(e){
        console.log("On add button clicked");
        var _steps = this.state.steps;
        var _id = Math.round(1000000*Math.random());
        _steps.push({
            id: _id,
            mode: "edit",
            type: "",
            description: ""
        });

        this.setState({
            steps: _steps
        });
    },
    deleteStep: function(step){
        console.log(step);
        console.log("delete button clicked");

        var _steps = this.state.steps.filter(function(_step){
            if(_step.id==step.id){
                return false;
            }
            return true;
        });

        this.setState({
            steps: _steps
        });
    },
    updateStep: function(step){
        console.log(step);
        console.log("step updated");

       var _steps = this.state.steps.map(function(_step){
            if(_step.id==step.id){
                return step;
            }
            return _step;
        });

        console.log(_steps);
        this.setState({
            steps: _steps
        });
    },
    render: function() {
        var _self = this;

        console.log("render scenario panel");
        // console.log(this.state.steps);

        var stepList = this.state.steps.map(function(step){
            return <TOD.react.StepInfo key={step.id} data={step} onContentChange={_self.updateStep} onDeleteButtonClick={_self.deleteStep}/>
        });

        return (
            <div className="panel panel-default">
                <div className="panel-heading">
                    <h3 className="panel-title" style={{"display": "inline-block"}}>Scenario</h3>
                    <button className="btn btn-sm btn-default" style={{"right": "24px","position": "absolute"}}>
                        <span className="glyphicon glyphicon-minus"></span>
                    </button>
                </div>
                <div className="panel-body">
                    <div className="btn-group" role="group" style={{"display":"flex", "marginBottom": "5px"}} >
                         <button onClick={this.onAddButtonClick} name="add-step" type="button" className="btn btn-default">Add Step</button>
                    </div>
                    {stepList}
                </div>
            </div>
        );
    }
});


ReactDOM.render(
   React.createElement(TOD.react.ScenarioContainer, null),
   document.getElementById('featureContainer')
);

