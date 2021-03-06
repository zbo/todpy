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
from auto.saver import StepDtoPostSaver
from workspace.saver import WorkSpaceGenerater
from auto.generator import FeatureFileGenerator
from config.models import AppSetting, FeatureLocation
from workspace.models import WorkSpace
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.db.models import Avg, Count, F, Max, Min, Sum, Q, Prefetch
from django.core.urlresolvers import reverse
from django.db import transaction
from django.contrib import admin


def test():
    django.setup()
    all_steps = '''{
        "feature": {
            "feature_name": "first feature name",
            "feature_description": "I want to test this first test case for fun",
            "feature_id": "new",
            "scenarios": [
                {
                    "scenario_name": "first scenario",
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
                                "action_type": "Then",
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
                                "action_type": "When",
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
                                "co_variables":{"text":"button"},
                                "description":"I click element with text 'button'"
                            }
                        },
                        {
                            "new": {
                                "action_type": "Then",
                                "co_firstlineno": 18,
                                "co_name": "i_close_browser",
                                "step_name": "I close web browser",
                                "co_argcount": 1,
                                "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                "co_varnames": [
                                    "step"
                                ],
                                "co_variables":{},
                                "description":"I close web browser"
                            }
                        }
                    ]
                },
                {
                    "scenario_name": "second scenario",
                    "scenario_id": "new",
                    "steps": [
                        {
                            "new": {
                                "action_type": "When",
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
                                "action_type": "Then",
                                "co_firstlineno": 13,
                                "co_name": "i_open_page",
                                "step_name": "I open page '([^']*)'",
                                "co_argcount": 2,
                                "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                "co_varnames": [
                                    "step",
                                    "url"
                                ],
                                "co_variables": {"url":"http://www.baidu.com"},
                                "description": "I open page 'http://www.baidu.com/'"
                            }
                        }
                    ]
                }
            ]
        }
    }'''
    workspace = WorkSpaceGenerater.gen_workspace('web')
    saver = StepDtoPostSaver()
    result = saver.save(all_steps)
    result.update_workspace(workspace)
    FeatureFileGenerator.save_feature_file(result, workspace, all_steps)
    # print result
    return result


if __name__ == '__main__':
    test()
