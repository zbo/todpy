__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time
import sys
sys.path.append(sys.path[0] + "/../decorator")
import global_decorator

@step("I record log \'([^\']*)\'")
def i_record_log(step, message):
    i_record_log_impl(step, message)


@global_decorator.logit
def i_record_log_impl(step, message):
    print message
