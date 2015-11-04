from django.db import models

import sys
sys.path.append('../')
sys.path.append('../../')

class FeatureLocation(models.Model):
    type=models.CharField(max_length=255)
    location=models.CharField(max_length=755)

class AppSetting(models.Model):
    type=models.CharField(max_length=255)
    value=models.CharField(max_length=255)