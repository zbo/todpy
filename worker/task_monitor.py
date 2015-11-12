__author__ = 'bob.zhu'
from datetime import datetime
import time
from plan_retriver import *
import thread

def work():
  print "hello world."
  iter_now = datetime.now()
  iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
  print iter_now_time
  single_plan = sqlite_execution_plan_retriver.retrive_first_one()



def runTask(func, rest_time):
  while True:
    time.sleep(rest_time)
    func()
    continue

runTask(work, rest_time=2)
