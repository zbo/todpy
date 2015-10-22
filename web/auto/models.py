from django.db import models

# Create your models here.
class Steps(models.Model):
    function = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    @staticmethod
    def getStepByFolder():
        return None