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
from auto.saver import StepDtoPostSaver
from workspace.saver import WorkSpaceGenerater
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
        "feature_id": "new",
        "feature_name": "Update apps order in App Gallery",
        "feature_description": "As a Product manager I want to re-order the public apps so that RC apps come first, then followed by 3rd party apps and coming soon apps.",
        "scenarios": [
            {
                "scenario_name": "name of scenario",
                "scenario_id": "UBP-XXXX",
                "steps": [
                    {
                        "5": {
                            "selected": true,
                            "disabled": false,
                            "text": "I open page '[?]'",
                            "co_firstlineno": 13,
                            "co_name": "i_open_page",
                            "step_name": "I open page '([^']*)'",
                            "action_type": "When",
                            "co_argcount": 2,
                            "co_file_name": "/Users/ian.zhang/Documents/workspace/todpy/libraries/web/action/features/web_browser.py",
                            "co_varnames": [
                                "step",
                                "url"
                            ],
                            "id": "4",
                            "value": "I open page '([^']*)'",
                            "co_variables": {
                                "url": "123"
                            },
                            "description": "I open page '123'"
                        }
                    }
                ]
            }
        ]
    }
}'''
    import pdb
    pdb.set_trace()
    workspace = WorkSpaceGenerater.gen_workspace('web')

    saver = StepDtoPostSaver()


    result = saver.save(all_steps)

    result.update_workspace(workspace)
    #plain_text = result.generate_feature()
    #print result
    return result


if __name__ == '__main__':
    test()
