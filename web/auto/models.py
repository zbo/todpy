import pdb
import sys
import lettuce

sys.path.append('../')
sys.path.append('../../')
from steploader import load_steps
from config.models import FeatureLocation
from django.db import models

# Create your models here.

class Step(models.Model):
    def __init__(self,function,description):
        self.function=function
        self.description=description

    function = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    module=models.CharField(max_length=255)
    location = models.TextField()

    @staticmethod
    def getStepByFolder(base_path):
        resultDict={}
        tags = None
        l_runner = lettuce.Runner(
            base_path=base_path
        )
        modules = load_steps(base_path)
        for i in range(len(modules)):
            mergedDict=resultDict.copy()
            mergedDict.update(modules[i].STEP_REGISTRY)
            resultDict=mergedDict
        return resultDict

    @staticmethod
    def searchStep(key_word,type):
        pdb.set_trace()
        dict=Step.getStepByFolder('../simple-selenium')
        keys=dict.keys()
        #pdb.set_trace()
        result={}
        for key in keys:
            result[key]=dict[key].func_name
        return result


class Feature(models.Model):
    description = models.CharField(max_length=255)
    module=models.CharField(max_length=255)
    location = models.TextField()

class Scenario(models.Model):
    scenario = models.CharField(max_length=255)
    feature = models.ForeignKey(Feature, related_name=("feature_scenario"))
    description = models.CharField(max_length=255)
    location = models.TextField()
    #TODO dataset
