// var React = require('react');

var GridLinkComponent = React.createClass({
    displayName: 'GridLinkComponent',
    render:function() {
    	var url = this.props.data.url
        return (
            <a href={url}>{this.props.data}</a>
      );
   	}
});

// module.exports = GridLinkComponent