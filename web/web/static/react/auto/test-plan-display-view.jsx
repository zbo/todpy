var TestplanDisplayView = React.createClass({
    displayName: 'TestplanDisplayView',
    getInitialState: function(){
      featureId = getEndingFromUrl();
      releaseList = [1,2,3,4,5];
      versionList = [1.1,2.1,3.2,4.2,5.2];
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
          name: name
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
                    <input type="text" className="form-control" id="input-name" placeholder="Name of Test Plan" value={this.state.name}/>
                  </div>
                </div>
                <div className="form-group">
                  <label htmlFor="input-description" className="col-sm-2 control-label">Description</label>
                  <div className="col-sm-8">
                    <textarea type="textarea" className="form-control" id="input-description" placeholder="Description" row="5">{this.state.description}</textarea>
                  </div>
                </div>
                <div className="form-group">
                  <label htmlFor="copy-from-test-plan" className="col-sm-2 control-label">Release Name:</label>
                  <div className="col-sm-8">
                    <select className="form-control" id="copy-from-test-plan" placeholder="Version">
                      {releaseOptionView}
                    </select>
                  </div>
                </div>
                <div className="form-group">
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
                  <label htmlFor="select-version" className="col-sm-2 control-label">Version Name:</label>
                  <div className="col-sm-8">
                    <select className="form-control" id="select-version" placeholder="Version">
                      {versionOptionView}
                    </select>
                  </div>
                </div>

                <div className="form-group">
                  <label className="col-sm-2 control-label">Test plan for Regression Cycle</label>
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
                  <div className="col-sm-offset-2 col-sm-10">
                    <button onClick={this.saveTestPlan} className="btn-xs btn-primary"><span className="glyphicon glyphicon-floppy-save"/>Save</button>
                    <button onClick={this.cancelTestPlan} className="btn-xs btn-danger"><span className="glyphicon glyphicon-remove"/>Cancel</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

      );//end of return
    }
})

ReactDOM.render(
    React.createElement(TestplanDisplayView, null),
    document.getElementById('test-plan-display-view')
);
