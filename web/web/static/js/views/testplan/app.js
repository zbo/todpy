$(document).ready(function(){
	var fakedata = [
		{
			id: 0,
			name: "Amarosa Release 7.3 RC1",
			Description: "",
			TestCaseQty: 266,
			Active: false,
			Public: true,
			// Control: control_btn_group
		},
		{
			id: 1,
			name: "Amarosa Release 7.4 RC1",
			Description: "",
			TestCaseQty: 578,
			Active: false,
			Public: true,
			// Control: control_btn_group
		},
		{
			id: 2,
			name: "Amarosa Release 7.5 RC1",
			Description: "",
			TestCaseQty: 728,
			Active: true,
			Public: true,
			// Control: control_btn_group
		},
		{
			id: 4,
			name: "Amarosa Release 7.5 RC2",
			Description: "",
			TestCaseQty: 728,
			Active: true,
			Public: true,
			// Control: control_btn_group
		}
	];

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
	  		"customComponent": GridLinkComponent
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

	ReactDOM.render(
		React.createElement(Griddle, 
		{ results: fakedata,
		  columns: ["id","name","Description","TestCaseQty","Active","Public"],
		  columnMetadata: columnMeta
		}),
		document.getElementById('test-plan-list-view')
	);
});