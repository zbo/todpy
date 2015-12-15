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
function NotConnected(all, connected){
  var ret = [];
  for(var i=0; i<all.length; i++){
    if($.inArray(all[i],connected)!=-1) continue;
    ret.push(all[i]);
  }
  return ret;
};
function RemoveArrayByElement(all, item){
  var ret=[];
  for(var i=0; i<all.length; i++){
    if(all[i]==item) continue;
    ret.push(all[i]);
  }
  return ret;
};
var TestPlanManageDialog = React.createClass({
    displayName: 'TestPlanManageDialog',
    getInitialState: function(){
      return {
        testcaseall:this.props.data.testcaseall,
        testcaseconnected:this.props.data.testcaseconnected,
        testcaseNotconnected:NotConnected(this.props.data.testcaseall,
          this.props.data.testcaseconnected)
      };
    },
    disconnectFeature: function(sender){
      var connected = this.state.testcaseconnected;
      var selected =sender.target.innerHTML;
      var notconnected = this.state.testcaseNotconnected;
      notconnected.push(selected);
      connected = RemoveArrayByElement(connected,selected);
      this.setState({testcaseconnected:connected});
      this.setState({testcaseNotconnected:notconnected});
    },
    connectFeature: function(sender){
      var connected = this.state.testcaseconnected;
      var selected =sender.target.innerHTML;
      connected.push(selected);
      var notconnected = this.state.testcaseNotconnected;
      notconnected = RemoveArrayByElement(notconnected,selected);
      this.setState({testcaseconnected:connected});
      this.setState({testcaseNotconnected:notconnected});
    },
    render: function(){
      var _self = this;

      var fearureconnected = this.state.testcaseconnected.map(function(item){
        return <button key={item} onClick={_self.disconnectFeature} className="btn btn-default" role="button">{item}</button>
      });
      var featureNotconnected = this.state.testcaseNotconnected.map(function(item){
        return <button key={item} onClick={_self.connectFeature} className="btn btn-default" role="button">{item}</button>
                                             });
      return(
        <div className="form-vertical">
        <div className="form-horizontal">
            <div className="col-sm-6 bg-info">Not connected</div>
            <div className="col-sm-6 bg-success">connected</div>
        </div>
        <div className="form-horizontal">
            <div className="col-sm-6 well">{featureNotconnected}</div>
            <div className="col-sm-6 well">{fearureconnected}</div>
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
      testcaseall = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
        'AX-0987','AX-0988','AX-0989','AX-0990',
        'XMN-0988','XMN-0986','XMN-0985','XMN-0984','XMN-0990',
        'XMN-0991','XMN-0992','XMN-0993','XMN-0994','XMN-0995'];
      testcaseconnected = [3,4,5,6,8,9,10,11,12,14,15,16,
        'AX-0987','AX-0988','AX-0989','AX-0990',
        'XMN-0988','XMN-0986','XMN-0985','XMN-0984','XMN-0990',
        'XMN-0991','XMN-0992','XMN-0993','XMN-0994','XMN-0995'];

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
                  			<h4 className="modal-title" id="myModalLabel">Features connect manage</h4>
                  		</div>
                  		<div className="">
                  		    <TestPlanManageDialog data={this.state}/>
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
