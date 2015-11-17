__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time
import sys
sys.path.append(sys.path[0] + "/../log")
import sqlite_logger

@step("I record log \'([^\']*)\'")
def i_record_log(step, message):
    i_record_log_impl(message)


@sqlite_logger.logit
def i_record_log_impl(message):
    print message
