__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time
import pdb

@step("I input \'([^\']*)\' into textbox with id \'([^\']*)\'")
def i_type_text(step, text, id):
    element = world.browser.find_element_by_id(id)
    element.click()
    element.send_keys(text)

