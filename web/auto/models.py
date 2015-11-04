import pdb
import sys
import lettuce

sys.path.append('../')
sys.path.append('../../')
from steploader import load_steps
from config.models import FeatureLocation
from auto.dto import StepDto
from django.db import models

# Create your models here.

class Feature(models.Model):
    def fill(self, description, module, location):
        self.description = description
        self.module = module
        self.location = location
        return self

    description = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    location = models.TextField()


class Scenario(models.Model):
    def fill(self, feature, description, location):
        self.feature = feature
        self.description = description
        self.location = location
        return self

    feature = models.ForeignKey(Feature)
    description = models.CharField(max_length=255)
    location = models.TextField()


class Step(models.Model):
    def fill(self, scenario, description, function, module, location):
        self.scenario = scenario
        self.description = description
        self.function = function
        self.module = module
        self.location = location
        return self

    scenario = models.ForeignKey(Scenario)
    description = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    location = models.TextField()

    @staticmethod
    def getStepByFolder(base_path):
        resultDict = {}
        modules = load_steps(base_path)
        for i in range(len(modules)):
            mergedDict = resultDict.copy()
            mergedDict.update(modules[i].STEP_REGISTRY)
            resultDict = mergedDict
        return resultDict

    @staticmethod
    def searchStep(key_word, type):
        feature_locations = FeatureLocation.objects.filter(type=type)
        result = {}
        for fl in feature_locations:
            dict = Step.getStepByFolder('../' + fl.location)
            keys = dict.keys()
            temp = {}
            for key in keys:
                # pdb.set_trace()
                step_dto = StepDto()
                step_dto.co_filename = dict[key].func_code.co_filename
                step_dto.co_firstlineno = dict[key].func_code.co_firstlineno
                step_dto.co_argcount = dict[key].func_code.co_argcount
                step_dto.co_varnames = dict[key].func_code.co_varnames
                step_dto.co_name = dict[key].func_code.co_name
                step_dto.step_name = key
                temp[key] = step_dto
            result = result.copy()
            result.update(temp)
        return result
