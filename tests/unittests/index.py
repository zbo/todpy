#!/usr/bin/env python 
# encoding: utf-8
import unittest
import sys
import os
import django
import json
import uuid
sys.path.append('../../web')
sys.path.append('../')
sys.path.append('../../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
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


class app_setting_tests(unittest.TestCase):
    def setUp(self):
        django.setup()
        pass

    def tearDown(self):
        pass

    def test_app_setting(self):
        results= AppSetting.getSetting('workspace')
        self.assertEqual(len(results),1)
        self.assertEqual(results[0],'workspaces')

    def test_gen_workspace(self):
        import test_gen_workspace
        test_gen_workspace.test()

    def test_step_dto(self):
        import test_step_dto
        test_step_dto.test()

    def test_step_dto_post_convert(self):
        import test_step_dto_post_convert
        test_step_dto_post_convert.test()
if __name__ == '__main__':
    unittest.main()
