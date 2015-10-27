    var Step_list = React.createClass({
    render: function () {
      return ( <div className="col-sm-8">
        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">Panel title</h3>
            </div>
            <div className="panel-body">
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>1,001</td>
                        <td>Lorem</td>
                        <td>ipsum</td>
                        <td>dolor</td>
                        <td>sit</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>);
    }
    });
    ReactDOM.render(
    <Step_list />,
    document.getElementById('steps_list')
    );