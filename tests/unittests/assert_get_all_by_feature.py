__author__ = 'bob.zhu'
from auto.models import Feature, Scenario, Step
import json

def assert_before_update(instance, json_str):
    json_data= json.loads(json_str)
    instance.assertEqual(len(json_data["scenarios"]),2)
    instance.assertEqual(len(json_data["scenarios"][0]['steps']),4)
    instance.assertEqual(json_data["scenarios"][0]['steps'][0]['co_name'],'i_open_browser')
    instance.assertEqual(json_data["scenarios"][0]['steps'][1]['co_name'],'i_open_page')
    instance.assertEqual(json_data["scenarios"][0]['steps'][2]['co_name'],'i_click_element_with_text')
    instance.assertEqual(json_data["scenarios"][0]['steps'][3]['co_name'],'i_close_browser')
    instance.assertEqual(json_data["scenarios"][1]['steps'][0]['co_name'],'i_open_browser')
    instance.assertEqual(json_data["scenarios"][1]['steps'][1]['co_name'],'i_open_page')
    pass