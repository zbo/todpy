import pdb
import sys
import lettuce

sys.path.append('../')
sys.path.append('../../')
from steploader import load_steps
<<<<<<< HEAD
from config.models import FeatureLocation
from django.db import models
=======
# import jsons
>>>>>>> add react for scenario editing

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
        modules = load_steps(base_path)
        for i in range(len(modules)):
            mergedDict=resultDict.copy()
            mergedDict.update(modules[i].STEP_REGISTRY)
            resultDict=mergedDict
        return resultDict

    @staticmethod
    def searchStep(key_word,type):
        feature_locations=FeatureLocation.objects.filter(type=type)
        result = {}
        for fl in feature_locations:
            dict=Step.getStepByFolder('../'+fl.location)
            keys=dict.keys()
            temp={}
            for key in keys:
                #pdb.set_trace()
                temp[key]=dict[key].func_name
            result=result.copy()
            result.update(temp)
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
