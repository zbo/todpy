__author__ = 'bob.zhu'
import json
class mocker:
    @staticmethod
    def get_mock_testplan_list():
        json_data = json.loads('''[
    {
        "id": 0,
        "name": "Amarosa Release 7.3 RC1",
        "Description": "",
        "TestCaseQty": 266,
        "Active": false,
        "Public": true
    },
    {
        "id": 1,
        "name": "Amarosa Release 7.4 RC1",
        "Description": "",
        "TestCaseQty": 267,
        "Active": false,
        "Public": true
    }
]''')
        return json_data
