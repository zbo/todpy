__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time
import pdb
import sys
sys.path.append(sys.path[0] + "/../log")
import sqlite_logger

@step("I input \'([^\']*)\' into textbox with id \'([^\']*)\'")
def i_type_text(step, text, id):
    i_type_text_impl(id, text)


@sqlite_logger.logit
def i_type_text_impl(id, text):
    element = world.browser.find_element_by_id(id)
    element.click()
    element.send_keys(text)
