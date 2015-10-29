__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time

@step("I record log \'([^\']*)\'")
def i_record_log(step, message):
    print message
