__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time


@step("I input text into textbox with id \'([^\']*)\'")
def i_type_text(step, id):

    element = world.browser.find_element_by_id(id)
