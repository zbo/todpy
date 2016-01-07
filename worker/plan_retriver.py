__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

sys.path.append('../web/web/')
sys.path.append('../web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from workspace.models import WorkSpace, Execution


class sqlite_execution_plan_retriver:
    @staticmethod
    def retrive_first_one():
        return Execution.objects.filter(status='planed').order_by('starttime').first()

    @staticmethod
    def mark_execution_as_running(execution):
        execution.status='running'
        execution.save()

    @staticmethod
    def mark_execution_as_finished(execution):
        execution.status='finished'
        execution.save()



if __name__ =='__main__':
    execution = sqlite_execution_plan_retriver.retrive_first_one()
    print execution.endtime