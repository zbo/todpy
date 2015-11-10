__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

sys.path.append('../web/')
sys.path.append('../../')
sys.path.append('../web/web/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from auto.generator import FeatureFileGenerator
from workspace.models import WorkSpace

def test():
    django.setup()
    feature = Feature.objects.get(pk=1)
    generate_feature_plain_text = FeatureFileGenerator.generate_feature(feature)
    workspace = WorkSpace.objects.first()
    feature = Feature.objects.first()
    FeatureFileGenerator.save_feature_file(feature,workspace)
    return generate_feature_plain_text

if __name__ == '__main__':
    test()