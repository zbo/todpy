var LinkComponent = React.createClass({
  render: function(){
    url ="testplan/" + this.props.rowData.id;
    return <a href={url}>{this.props.data}</a>
  }
});

var columnMeta = [
  {
    "columnName": "id",
      "order": 1,
      "locked": false,
      "visible": true
  },{
    "columnName": "name",
      "order": 2,
      "locked": false,
      "visible": true,
      "customComponent": LinkComponent
  },{
    "columnName": "Description",
      "order": 3,
      "locked": false,
      "visible": true
  },{
    "columnName": "TestcaseQty",
      "order": 4,
      "locked": false,
      "displayName":"Test case qty",
      "visible": true
  }, {
    "columnName": "Active",
      "order": 5,
      "locked": false,
      "visible": true
  }, {
    "columnName": "Public",
      "order": 6,
      "locked": false,
      "visible": true
  }
];

var TestplanListView = React.createClass({
  displayName: 'TestplanListView',

  getInitialState: function(){
    var testPlanData;
    var testPlanService = new TOD.service.testPlanService();
    testPlanData = testPlanService.getAllTestPlans();
    return {
      testPlanData:testPlanData
    };
  },

  createTestPlan: function(){
    var url = window.location.protocol+"//"+window.location.host+"/auto/testplan/create";
		window.location = url;
  },

  render: function(){
      var TestPlanGriddle = React.createElement(Griddle,
      { results: this.state.testPlanData,
        columns: ["id","name","Description","TestCaseQty","Active","Public"],
        columnMetadata: columnMeta,
        showFilter: true
      });
      return(
        <div className="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
        	<div className="page-header">
        		<div className="btn-group pull-right">
        			<button id="create-testplan-btn" onClick={this.createTestPlan} className="btn btn-default">Create New Test Plan</button>
        		</div>
        		<h1>Test Plan List</h1>
        	</div>
          {TestPlanGriddle}
        </div>
      );
  }
})
ReactDOM.render(
    React.createElement(TestplanListView, null),
    document.getElementById('test-plan-list-view')
);
