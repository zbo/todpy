__author__ = 'bob.zhu'
__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid

sys.path.append('../web/')
sys.path.append('../web/web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto, FeatureDto, ScenarioDto, DataEncoder
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
    feature_id = 1
    feature = Feature.objects.filter(id=feature_id).first()
    feature_dto = FeatureDto(feature.name, feature.description)
    scenarios = []
    for sce in feature.scenario_set.filter(deleted=0):
        s_dto = ScenarioDto(sce.description)
        s_dto.fill_steps(sce)

        scenarios.append(s_dto)
    feature_dto.fill_scenarios(scenarios)
    print json.dumps((feature_dto),cls=DataEncoder)
    return json.dumps((feature_dto),cls=DataEncoder)


if __name__ == '__main__':
    test()
