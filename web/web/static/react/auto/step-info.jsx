// var React = require('react');
var TOD = TOD || {};
TOD.react = TOD.react || {};
TOD.react.data = TOD.react.data || {};

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
        var _index = Math.round(10000000*Math.random());
        return {
            index: _index,
            definedSteps: [],
            data: {
                id: -1,
                type: "",
                description: "desc1",
                step: {}
            }  
        };
    },
    componentWillMount: function() {

        if(!this.props.data.id){
            this.props.data.id = Math.round(1000000*Math.random());
        }
        var _definedSteps = (new TOD.service.StepService()).getDefinedStepsByPlatform("web")
        this.setState({
            definedSteps: _definedSteps,
            data:{
                id: this.props.data.id,
                key: this.props.data.key,
                type:this.props.data.type,
                description: this.props.data.description,
                step: this.props.data.step,
            }
        });
    },
    // handleItemChange: function(e){
    //     var updateProp = e.target.dataset.name;
    //     console.log(updateProp);
        
    //     this.state.data[updateProp] = e.target.value;
    //     this.setState({
    //       data: this.state.data
    //     });
    // },
    handleTypeSelections: function(e, selections){
        this.setState({
            data: {
                id: this.state.data.id,
                key: this.props.data.key,
                type: selections[0].value,
                description: this.state.data.description,
                step:this.state.data.step
            }
        });
    },
    handleStepSelections: function(e, selections, next){
        // console.log("handle step selection")
        // console.log(selections);
        
        var _selected = selections[0];

        this.setState({
            data: {
                id: this.state.data.id,
                key: this.props.data.key,
                type: this.state.data.type,
                description: this.state.data.step.description,
                step: _selected
            }
        });
    },
    handleStepParameterChange: function(e, g){
        var $dom = e.target;
        var arg = $dom.dataset["name"];

        this.state.data.step.co_variables[arg] = e.target.value;
        this.setState({data: this.state.data});
    },
    saveChange: function(e){
        var _step = this.state.data.step;
        TOD.util.stepParser.parseDescription(_step);
        this.state.data.description = _step.description;
        this.props.onContentChange(this.state.data);
        this.props.onChangeMode("display");
    },
    discardChange: function(e){
        this.props.onChangeMode("display");  
    },
    render: function() {
        var type = this.state.data.type,
            description = this.state.data.description,
            _step = this.state.data.step,
            _self = this;

        var supportedType = [
            {id: 0, text: "Given", value: "Given"},
            {id: 1, text: "When", value: "When"},
            {id: 2, text: "Then", value: "Then"}
        ];
        var typeIndex = [supportedType.findIndex(function(e){
            return e.text===type;
        })];


        var providedSteps = this.state.definedSteps;
        var stepIndex = [providedSteps.findIndex(function(step){
            return _step.value===step.value;  
        })];

        var stepParameters = TOD.util.stepParser.extractParameters(_step);

        var selectTypeId = "select-step-type-"+this.state.index,
            selectStepId = "select-step-"+this.state.index,
            editorPrefix = this.state.data.id;

        var parameterList = stepParameters.map(function(para){
            var _key = editorPrefix+"_"+para.arg+"_input";
            var _data = para.value;
            return (
                <div key={_key} className="parameter_list" style={{"marginTop":"5px"}}>
                    <div className="form-horizontal">
                      <div className="form-group">
                        <label className="col-sm-2 control-label">{para.arg}: </label>
                        <div className="col-sm-10">
                          <input id={_key} onChange={_self.handleStepParameterChange} data-name={para.arg} type="text" className="form-control" value={_data}></input>
                        </div>
                      </div>
                    </div>
                </div>
            );
        });

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
                            val={typeIndex}
                            data-name="type"/>
                    </div>
                    <div className="col-sm-9">
                        <h4>Select Step</h4>
                        <Select2Component id={selectStepId}
                            styleWidth="100%"
                            placeholder="select step"
                            onSelection = {this.handleStepSelections}
                            dataSet={providedSteps}
                            multiple={false}
                            val={stepIndex}
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
        if(this.props.data && this.props.data.co_variables && "string" === (typeof this.props.data.co_variables)){
            var _step = {}
            
            for(var attribute in this.props.data){
                _step[attribute] = this.props.data[attribute];
            }
            _step.co_variables = JSON.parse(this.props.data.co_variables);
            _step.value = _step.step_name;
            delete _step.id;
            this.props.data.step = _step;
            this.props.data.type = this.props.data.action_type;
        }

        this.setState({
            mode: (this.props.data.mode || "display"),
            data: {
                id: this.props.data.id,
                key: this.props.data.key,
                type: this.props.data.type,
                description: this.props.data.description,
                step: this.props.data.step
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
                key: _data.key,
                type: _data.type,
                description: _data.description,
                step: _data.step
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

var ScenarioContainer = React.createClass({
    displayName: 'ScenarioContainer',
    getInitialState() {
        return {
            id: "",
            name: "",
            description: "",
            steps: [
                {
                    id: 'new',
                    mode: "display",
                    type: "Given",
                    description: "I open web brower",
                    step: {
                        "action_type": "Given",
                        "co_firstlineno": 8,
                        "co_name": "i_open_browser",
                        "step_name": "I open web browser",
                        "co_argcount": 1,
                        "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                        "co_varnames": [
                            "step"
                        ],
                        "co_variables":{},
                        "description":"I open web browser",
                        "value": "I open web browser"
                    }
                }
            ]
        };
    },
    getScenarioData: function(){
        // console.log(this.state.steps);
        TOD.react.data.scenarios = TOD.react.data.scenarios || [];
        var _self = this;
        var _index = TOD.react.data.scenarios.findIndex(function(scenario){
            if(!_self.state.id){
                return false;
            }

            if(_self.state.id===scenario.id){
                return true;
            }
        });

        if( _index < 0){
            TOD.react.data.scenarios.push(this.state);
        } else{
            TOD.react.data.scenarios[_index] = this.state;
        }

    },
    componentWillMount:function() {
        PubSub.subscribe(TOD.events.getScenarioData, this.getScenarioData);
    },
    componentDidMount: function() {
        if(this.props.data){
            this.setState({
                id: this.props.data.id,
                name: this.props.data.description,
                description: this.props.data.description,
                steps: this.props.data.steps
            });
        }
    },
    onAddButtonClick: function(e){
        console.log("On add button clicked");
        var _steps = this.state.steps;
        
        var _id='new',
            _key = Math.round(1000000*Math.random());
        _steps.push({
            id: _id,
            key:_key,
            mode: "edit",
            type: "",
            description: "",
            step:{}
        });

        this.setState({
            steps: _steps
        });
    },
    deleteStep: function(step){
        console.log(step);
        console.log("delete button clicked");


        var _steps = this.state.steps.filter(function(_step){
            if(('new'!==step.id &&_step.id===step.id)
                || ('new' === step.id && 'new' === step.id && _step.key===step.key)){
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
            if(('new'!==step.id &&_step.id===step.id)
                || ('new' === step.id && 'new' === step.id && _step.key===step.key)){
                return step;
            }
            return _step;
        });

        this.setState({
            steps: _steps
        });
    },
    saveScenario: function(e){
        // @Deprecated
        console.log("Save Scenario Info");
        console.log(this.state.steps);
    },
    editScenario:function(e){
        console.log("edit scenario Info");

        this.setState({
            "editing": true,
            new_name: this.state.name
        });
    },
    cancelEdit: function(e){
        console.log("cancelEdit");
        var _state = this.state;
        if(this.state.editing){
            delete _state.editing;
            this.setState(_state);
        }
    },
    confirmEdit: function(e){
        console.log("confirmEdit");        
        var _state = this.state;

        if(this.state.editing){
            _state.name = _state.new_name;
            delete _state.editing;
            delete _state.new_name;
            this.setState(_state);
        }
    },
    onValueChange:function(e){
        console.log(e);
        this.setState({
            new_name:e.target.value
        });
    },
    togglePanel: function(e){
        // console.log(this.getDOMNode());
        $(ReactDOM.findDOMNode(this)).find(".panel-body").toggle();
    },
    render: function() {
        var _self = this;

        console.log("render scenario panel");
        // console.log(this.state.steps);
        
        var stepList = this.state.steps.map(function(step){
            var key = _self.state.id+"_"+('new'===step.id? step.key : step.id);
            return <TOD.react.StepInfo key={key} data={step} onContentChange={_self.updateStep} onDeleteButtonClick={_self.deleteStep}/>
        });

        var scenario_info = (function(){
            console.log(_self.state)
            if(_self.state.editing){
                return (
                    <div className="input-group">
                      <input type="text" onChange={_self.onValueChange} className="form-control" placeholder="Scenario name..." value={_self.state.new_name}></input>
                      <span className="input-group-btn">
                        <button onClick={_self.confirmEdit} className="btn btn-default" type="button"><span className="glyphicon glyphicon-ok"></span></button>
                        <button onClick={_self.cancelEdit} className="btn btn-default" type="button"><span className="glyphicon glyphicon-remove"></span></button>
                      </span>
                    </div>
                );
            } else {
                return (
                    <i>{_self.state.name}</i>
                );
            }
        })();

        return (
            <div className="panel panel-default">
                <div className="panel-heading">
                    <button onClick={this.togglePanel} className="btn btn-xs btn-default pull-right">
                        <span className="glyphicon glyphicon-minus"></span>
                    </button>

                    <h3 className="panel-title" style={{"display": "inline-block"}}>
                        Scenario: {scenario_info}
                    </h3>
                </div>
                <div className="panel-body">
                    <div className="btn-group" role="group" style={{"display":"flex", "marginBottom": "5px"}} >
                         <button onClick={this.onAddButtonClick} data-name="add-step" type="button" className="btn btn-default">Add Step</button>
                         <button onClick={this.editScenario} data-name="edit-scenario" type="button" className="btn btn-primary">Edit Scenario</button>
                         <button onClick={this.saveScenario} data-name="save-step" type="button" className="btn btn-primary hide">Save Scenario</button>                         
                    </div>
                    <div className="scenario-description hide">
                        <p>{this.state.description}</p>
                    </div>
                    {stepList}
                </div>
            </div>
        );
    }
});


// if(document.getElementById('scenarios-container')){
//     ReactDOM.render(
//        React.createElement(ScenarioContainer, null),
//        document.getElementById('scenarios-container')
//     );    
// }

