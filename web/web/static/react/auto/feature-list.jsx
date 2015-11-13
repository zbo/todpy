// var React = require('react');

var FeatureList = React.createClass({
    displayName: 'FeatureList',
    getInitialState: function() {
        return {
        	dataSource: []
        };
    },
    componentWillMount:function() {
    	var featureService = TOD.service.featureService();
    	try{
    		var _dataSource = featureService.getFeatureList();
    		_dataSource = _dataSource.map(function(data){
    			data.children=[];
    			data.text = data.id+" : "+data.name;
    			data.id = ""+data.id;
    			return data;
    		});

    		this.setState({
    			dataSource: _dataSource
    		});
    	} catch (e){
    		console.log("error");
    	}
    },
    handleTreenodeClick: function(id, node){
    	console.log("tree node clicked");
    	console.log(id);
    	var url = window.location.protocol+"//"+window.location.host+"/auto/feature/"+id+"/";
        window.location = url;
        
    },
    render: function() {
        return (
            <div>
            	<Treeview dataSource={this.state.dataSource}
				  onTreenodeClick={this.handleTreenodeClick}>
				</Treeview>
            </div>
        );
    }
});

	ReactDOM.render(
	   React.createElement(FeatureList, null),
	   document.getElementById('feature-tree-view')
	);

// module.exports = featureList;