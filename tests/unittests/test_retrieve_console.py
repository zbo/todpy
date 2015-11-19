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
from workspace.saver import WorkSpaceGenerater, Execution


def test():
    django.setup()
    feature_id = 1
    feature = Feature.objects.get(pk=feature_id)
    workspace_id = feature.workspace
    execution = Execution.objects.filter(workspace_id=workspace_id).order_by('starttime').last()
    testlog = execution.testlog_set.first()
    print testlog.content

if __name__ == '__main__':
    test()
