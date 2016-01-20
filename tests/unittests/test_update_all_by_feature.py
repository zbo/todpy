__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

current_dir = path = sys.path[0]
path_len= current_dir.index('todpy')+len('todpy')
root_path=current_dir[:path_len]
web_path=os.path.join(root_path,'web')
web_web_path=os.path.join(root_path,'web/web')
tests_path=os.path.join(root_path,'tests')
unittests_path=os.path.join(root_path,'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from auto.saver import StepDtoPostSaver, StepDtoPostUpdater
from config.models import AppSetting, FeatureLocation
from workspace.models import WorkSpace
from auto.generator import FeatureFileGenerator


def test():
    django.setup()
    all_steps = '''{
            "feature": {
                "feature_name": "test okcoin user reg form",
                "feature_description": "just for test",
                "feature_id": 1,
                "project_id": 1,
                "suite_id": 2,
                "scenarios": [
                    {
                        "scenario_name": "first updated scenario",
                        "scenario_id": 1,
                        "steps": [
                            {
                                "1": {
                                    "action_type": "Given",
                                    "co_firstlineno": 8,
                                    "co_name": "i_open_browser",
                                    "step_name": "I open web browser",
                                    "co_argcount": 1,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step"
                                    ],
                                    "co_variables":{},
                                    "description":"I open web browser"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "When",
                                    "co_firstlineno": 13,
                                    "co_name": "i_open_page",
                                    "step_name": "I open page '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step",
                                        "url"
                                    ],
                                    "co_variables": {"url":"http://www.okcoin.com/"},
                                    "description": "I open page 'http://www.okcoin.com/'"
                                }
                            },
                            {
                                "3": {
                                    "action_type": "Then",
                                    "co_firstlineno": 14,
                                    "co_name": "i_click_element_with_text",
                                    "step_name": "I click element with text '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                                    "co_varnames": [
                                        "step",
                                        "text",
                                        "element"
                                    ],
                                    "co_variables":{"text":"buy"},
                                    "description":"I click element with text 'Trade'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 14,
                                    "co_name": "i_click_element_with_text",
                                    "step_name": "I click element with text '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                                    "co_varnames": [
                                        "step",
                                        "text",
                                        "element"
                                    ],
                                    "co_variables":{"text":"Sign Up"},
                                    "description":"I click element with text 'Sign Up'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_close_browser",
                                    "step_name": "I input '([^']*)' into textbox with id '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_edit.py",
                                    "co_varnames": [
                                        "step",
                                        "text",
                                        "id"
                                    ],
                                    "co_variables":{},
                                    "description":"I input 'zbo2@qq.com' into textbox with id 'regUserName'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_close_browser",
                                    "step_name": "I input '([^']*)' into textbox with id '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_edit.py",
                                    "co_varnames": [
                                        "step",
                                        "text",
                                        "id"
                                    ],
                                    "co_variables":{},
                                    "description":"I input '123456' into textbox with id 'regPassword'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_close_browser",
                                    "step_name": "I input '([^']*)' into textbox with id '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_edit.py",
                                    "co_varnames": [
                                        "step",
                                        "text",
                                        "id"
                                    ],
                                    "co_variables":{},
                                    "description":"I input '123456' into textbox with id 'regRePassword'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_click_element_with_id",
                                    "step_name": "I click element with id '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                                    "co_varnames": [
                                        "step",
                                        "id"
                                    ],
                                    "co_variables":{},
                                    "description":"I click element with id 'agree'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_click_element_with_id",
                                    "step_name": "I click element with id '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_click.py",
                                    "co_varnames": [
                                        "step",
                                        "id"
                                    ],
                                    "co_variables":{},
                                    "description":"I click element with id 'regBtn'"
                                }
                            },
                            {
                                "4": {
                                    "action_type": "Then",
                                    "co_firstlineno": 4,
                                    "co_name": "i_close_browser",
                                    "step_name": "I close web browser",
                                    "co_argcount": 1,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step"
                                    ],
                                    "co_variables": {},
                                    "description": "I close web browser"
                                }
                            }
                        ]
                    },
                    {
                        "scenario_name": "second new created scenario",
                        "scenario_id": "new",
                        "steps": [
                            {
                                "new": {
                                    "action_type": "Given",
                                    "co_firstlineno": 8,
                                    "co_name": "i_open_browser",
                                    "step_name": "I open web browser",
                                    "co_argcount": 1,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step"
                                    ],
                                    "co_variables":{},
                                    "description":"I open web browser"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "When",
                                    "co_firstlineno": 13,
                                    "co_name": "i_open_page",
                                    "step_name": "I open page '([^']*)'",
                                    "co_argcount": 2,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step",
                                        "url"
                                    ],
                                    "co_variables": {"url":"http://cn.bing.com/"},
                                    "description": "I open page 'http://cn.bing.com/'"
                                }
                            },
                            {
                                "new": {
                                    "action_type": "Then",
                                    "co_firstlineno": 4,
                                    "co_name": "i_close_browser",
                                    "step_name": "I close web browser",
                                    "co_argcount": 1,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step"
                                    ],
                                    "co_variables": {},
                                    "description": "I close web browser"
                                }
                            }
                        ]
                    }
                ]
            }
        }'''

    updater = StepDtoPostUpdater()
    result = updater.update(all_steps)
    workspace = WorkSpace.objects.get(pk=result.workspace)
    FeatureFileGenerator.update_feature_file(result, workspace, all_steps)
    return result

if __name__ == '__main__':
    test()
