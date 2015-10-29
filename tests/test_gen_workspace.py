__author__ = 'bob.zhu'
import sys
import os
import django

sys.path.append('../web')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from config.models import AppSetting, FeatureLocation
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


def load_config():
    global config
    config = {}
    for setting in AppSetting.objects.all():
        config[setting.type] = setting.value

django.setup()
load_config()

print config
print FeatureLocation
feature_locations = FeatureLocation.objects.filter(type='ios')
result = {}
for fl in feature_locations:
    dict = Step.getStepByFolder('../' + fl.location)
    keys = dict.keys()
    temp = {}
    for key in keys:
        temp[key] = dict[key].func_name
    result = result.copy()
    result.update(temp)
print result
