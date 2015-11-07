__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

sys.path.append('../web')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from auto.saver import StepDtoPostSaver, StepDtoPostUpdater
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
                "feature_name": "change name feature name",
                "feature_description": "not fun now",
                "feature_id": 1,
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
                                    ]
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
                                    ]
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
                                    ]
                                }
                            },
                            {
                                "4": {
                                    "action_type": "Then",
                                    "co_firstlineno": 18,
                                    "co_name": "i_close_browser",
                                    "step_name": "I close web browser",
                                    "co_argcount": 1,
                                    "co_file_name": "/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py",
                                    "co_varnames": [
                                        "step"
                                    ]
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
                                    ]
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
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        }'''

    updater = StepDtoPostUpdater()
    result = updater.update(all_steps)
    return result
if __name__ == '__main__':
    test()