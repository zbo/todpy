__author__ = 'bob.zhu'
import os
import sys
sys.path.append('../web/web/')
sys.path.append('../web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from datetime import datetime
import time
from plan_retriver import *
import django

def work():
    single_plan = sqlite_execution_plan_retriver.retrive_first_one()
    if single_plan is None:
        heart_beat()
    else:
        sqlite_execution_plan_retriver.mark_execution_as_running(single_plan)
        print 'work execution found id:{0}, booked time:{1}, ==== start!'.format(single_plan.id, single_plan.starttime)


def heart_beat():
    iter_now = datetime.now()
    iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
    print iter_now_time
    print 'heart beat work plan cleaned ----- :-)'


def runTask(func, rest_time):
    django.setup()
    while True:
        time.sleep(rest_time)
        func()
        continue

runTask(work, rest_time=2)
