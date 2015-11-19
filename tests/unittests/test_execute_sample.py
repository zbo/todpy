__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

sys.path.append('../web/')
sys.path.append('../web/web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from auto.saver import StepDtoPostSaver
from workspace.saver import WorkSpaceGenerater
from workspace.executor import Executor
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
    command = 'lettuce ../../workspaces/01'
    Executor.execute(command)

if __name__ == '__main__':
    test()