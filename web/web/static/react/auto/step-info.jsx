// var React = require('react');
var TOD = TOD || {};
TOD.react = TOD.react || {};

var StepInfoDisplay = React.createClass({
    displayName: 'StepInfoDisplay',
    changeMode: function(e){
        this.props.onChangeMode("edit");
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
                <button onClick={_self.changeMode} data-next="edit"  className="btn btn-xs btn-primary">Edit</button>
                <button className="btn btn-xs btn-danger">X</button>
            </div>
        </div>
        );
    }
});

var StepInfoEdit = React.createClass({
    displayName: 'StepInfoEdit',
    getInitialState() {
        console.log("getInitialState");
        return {
            data: {
                type: "",
                description: "desc1"
            }  
        };
    },
    componentWillMount: function() {
        console.log("Edit will mount:")
        console.log(this.props.data);
        this.setState({
            data:{
                type:this.props.data.type,
                description: this.props.data.description
            }
        });
    },
    componentDidMount: function(prevProps, prevState) {
        // $("select").select2();  
    },
    handleItemChange: function(e){
        var updateProp = e.target.dataset.name;
        console.log(updateProp);
        
        this.state.data[updateProp] = e.target.value;
        this.setState({
          "data": this.state.data
        });
    },
    handleSelections: function(){

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
            {id: 0, text: "Given", val: "Given"},
            {id: 1, text: "When", val: "When"},
            {id: 2, text: "Then", val: "Then"}
        ];
        console.log("render");
        console.log(type+":"+description);
        return (
        <div className="row">
            <div className="col-md-10">
                <div className="row">
                    <div className="col-sm-3">
                        <h4>By Type</h4>
                        <Select2Component id="select-step-type" 
                            styleWidth="100%"
                            placeholder="select type"
                            onSelection = {this.handleSelections}
                            dataSet={supportedType}
                            val={[1]}
                            data-name="type"/>
                    </div>
                    <div className="col-sm-9">
                        <h4>Select Step</h4>
                        <select id="select-step" style={{"width":"100%"}} value={description} onChange={this.handleItemChange} data-name="description">
                            <option value="When I login as a valid user">When I login as a valid user</option>
                            <option value="When I have a developer account">When I have a developer account</option>
                        </select>
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
                type: "Given",
                description: "This is description from React"
            }
        };
    },
    componentWillMount: function(){
        this.setState({
            mode: this.props.data.mode,
            data: {
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
        this.setState({data:_data});
    },
    render: function() {
        // console.log("React Render")
        var _self = this;
        var component = (function(){
            switch (_self.state.mode)
            {
                case "display":
                    return (<StepInfoDisplay onChangeMode={_self.changeMode} data={_self.state.data}/>);
                case "edit":
                    return (<StepInfoEdit onContentChange={_self.handleContentChange} onChangeMode={_self.changeMode} data={_self.state.data}/>);
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
                    mode: "display",
                    type: "Given",
                    description: "a clean and valid account in system"
                },
                {
                    mode: "display",
                    type: "When",
                    description: "I login the system"
                },
                {
                    mode: "display",
                    type: "When",
                    description: "I have authorization of developer"
                }
            ]
        };
    },
    onAddButtonClick: function(e){
        console.log("On add button clicked");
        var _steps = this.state.steps;
        _steps.push({
            mode: "edit",
            type: "",
            description: ""
        });

        this.setState({
            steps: _steps
        });
    },
    render: function() {
        var index = 0;

        var stepList = this.state.steps.map(function(step){

            return <TOD.react.StepInfo key={index++} data={step} />
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

