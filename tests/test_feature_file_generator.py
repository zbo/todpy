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
from auto.generator import FeatureFileGenerator

def test():
    django.setup()
    feature = Feature.objects.get(pk=1)
    for line in FeatureFileGenerator.generate_feature(feature):
        print line
    pass

if __name__ == '__main__':
    test()