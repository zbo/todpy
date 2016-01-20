__author__ = 'bob.zhu'
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
from auto.dto import StepDto, FeatureDto, ScenarioDto, DataEncoder
from config.models import AppSetting, FeatureLocation
from workspace.models import WorkSpace
from workspace.saver import WorkSpaceGenerater, ExecutionPlanSaver

def test():
    django.setup()
    feature_id = 1
    result = ExecutionPlanSaver.save_execution_plan(feature_id)
    return result, feature_id

if __name__ == '__main__':
    test()