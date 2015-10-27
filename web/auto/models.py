from django.db import models
import pdb
import sys
import lettuce

sys.path.append('../')
sys.path.append('../../')
from steploader import load_steps

# Create your models here.
base_path = '../simple-selenium'

class Step(models.Model):
    function = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    module=models.CharField(max_length=255)
    location = models.TextField()

    @staticmethod
    def getStepByFolder():
        #pdb.set_trace()
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