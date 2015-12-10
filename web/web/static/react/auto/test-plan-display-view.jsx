var TestCaseConnectView = React.createClass({
    displayName: 'TestCaseConnectView',
    render: function(){
      var fearureconnected = this.props.data.map(function(item){
        return <a key={item} className="btn btn-default" role="button">{item}</a>
      });
      return (
        <div id="test-case-connected" className="well">
          <div className="form-horizontal">
            <div className="form-group">
              <label>Feature Connected:</label>
            </div>
            <div className="form-group">
              {fearureconnected}
            </div>
          </div>
        </div>
      );
    }

});

var TestplanDisplayView = React.createClass({
    displayName: 'TestplanDisplayView',
    getInitialState: function(){
      featureId = getEndingFromUrl();
      releaseList = [1,2,3,4,5];
      versionList = [1.1,2.1,3.2,4.2,5.2];
      testcaseall = [1,2,3,4,5,6,7,8];
      testcaseconnected = [3,4,5];

      var description, name;
      var testPlanFor = "0"
      if(!window.location.pathname.endsWith('create')){
          description = "some from server"
          name = "some from server"
          testPlanFor = "2"
      }
      return {
          mode:"display",
          featureId: "new",
          releaseList: releaseList,
          versionList: versionList,
          active: false,
          testPlanFor: testPlanFor,
          description: description,
          name: name,
          testcaseall: testcaseall,
          testcaseconnected: testcaseconnected
      };
    },

    cycleChange: function(sender){
      this.setState({testPlanFor:sender.target.value});
    },

    saveTestPlan: function(sender){
      var url = window.location.protocol+"//"+window.location.host+"/auto/testplans/";
      window.location = url;
    },

    cancelTestPlan: function(sender){
        var url = window.location.protocol+"//"+window.location.host+"/auto/testplans/";
    		window.location = url;
    },

    dataChange: function(sender){
        this.setState({description: $("#input-description").val()});
        this.setState({name: $("#input-name").val()});

    },

    render: function(){
        var releaseOptionView = this.state.releaseList.map(function(release){
          return (<option key={release}>{release}</option>)
        });
        var versionOptionView = this.state.versionList.map(function(version){
          return (<option key={version}>{version}</option>)
        });
        return (
          <div className="row">
            <h1 id="feature-page-header" className="page-header">Test Plan Detail</h1>
            <div id="test-plan-viewer" className="well">
              <div className="form-horizontal">
                <div className="form-group">
                  <label htmlFor="input-name" className="col-sm-2 control-label">Name</label>
                  <div className="col-sm-8">
                    <input type="text" onChange={this.dataChange} className="form-control" id="input-name" placeholder="Name of Test Plan" value={this.state.name}/>
                  </div>
                </div>
                <div className="form-group">
                  <label htmlFor="input-description" className="col-sm-2 control-label">Description</label>
                  <div className="col-sm-8">
                    <textarea type="textarea" onChange={this.dataChange} className="form-control" value={this.state.description} id="input-description" placeholder="Description" row="5"/>
                  </div>
                </div>
                <div className="form-group">
                  <label htmlFor="copy-from-test-plan" className="col-sm-2 control-label">Release Name</label>
                  <div className="col-sm-8">
                    <select className="form-control" id="copy-from-test-plan" placeholder="Version">
                      {releaseOptionView}
                    </select>
                  </div>
                </div>
                <div className="form-group hide">
                  <div className="col-sm-offset-2 col-sm-10">
                    <div className="checkbox">
                      <label>
                        <input type="checkbox"/>Active
                      </label>
                    </div>
                    <div className="checkbox">
                      <label>
                        <input type="checkbox"/>Private
                      </label>
                    </div>
                  </div>
                </div>

                <div className="form-group">
                  <label htmlFor="select-version" className="col-sm-2 control-label">Version Name</label>
                  <div className="col-sm-8">
                    <select className="form-control" id="select-version" placeholder="Version">
                      {versionOptionView}
                    </select>
                  </div>
                </div>

                <div className="form-group">
                  <label className="col-sm-2 control-label">Regression Cycle</label>
                  <div className="col-sm-10">
                      <label className="radio-inline">
                        <input type="radio" onChange={this.cycleChange} checked={this.state.testPlanFor==0} id="inlineRadio1" value="0"/>Not for regression
                      </label>
                      <label className="radio-inline">
                        <input type="radio" onChange={this.cycleChange} checked={this.state.testPlanFor==1} id="inlineRadio2" value="1"/>RC1
                      </label>
                      <label className="radio-inline">
                        <input type="radio" onChange={this.cycleChange} checked={this.state.testPlanFor==2} id="inlineRadio3" value="2"/>RC2
                      </label>
                  </div>
                </div>

                <div className="form-group">
                  <div className="col-sm-offset-2 col-sm-6">
                    <button type="button" className="btn btn-primary btn-sm" data-toggle="modal" data-target="#myModal">
                    manage features
                    </button>
                  </div>
                  <div className="modal fade" id="myModal" tabIndex="-1" role="dialog" aria-labelledby="myModalLabel">
                  <div className="modal-dialog" role="document">
                  	<div className="modal-content">
                  		<div className="modal-header">
                  			<button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  			<h4 className="modal-title" id="myModalLabel">Features connect to this test plan</h4>
                  		</div>
                  		<div className="modal-body">
                  			...
                  		</div>
                  		<div className="modal-footer">
                  			<button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
                  			<button type="button" className="btn btn-primary">Save changes</button>
                  		</div>
                  	</div>
                  </div>
                </div>
              </div>

                <div className="form-group">
                  <div className="col-sm-offset-2 col-sm-10">
                    <button onClick={this.saveTestPlan} className="btn-xs btn-primary"><span className="glyphicon glyphicon-floppy-save"/>Save</button>
                    <button onClick={this.cancelTestPlan} className="btn-xs btn-danger"><span className="glyphicon glyphicon-remove"/>Cancel</button>
                  </div>
                </div>
              </div>
            </div>
            <TestCaseConnectView data={this.state.testcaseconnected}/>
          </div>


      );//end of return
    }
})

ReactDOM.render(
    React.createElement(TestplanDisplayView, null),
    document.getElementById('test-plan-display-view')
);
