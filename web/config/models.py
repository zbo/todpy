from django.db import models

import sys
sys.path.append('../')
sys.path.append('../../')

class FeatureLocation(models.Model):
    type=models.CharField(max_length=255)
    location=models.CharField(max_length=755)

    @staticmethod
    def getLocation(type):
        result = []
        filter = FeatureLocation.objects.filter(type=type)
        for item in filter:
            result.append(item.location)

        return result

class AppSetting(models.Model):
    type=models.CharField(max_length=255)
    value=models.CharField(max_length=255)

    @staticmethod
    def getSetting(type):
        result = []
        filter = AppSetting.objects.filter(type=type)
        for item in filter:
            result.append(item.value)
        return result
