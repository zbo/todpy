__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time


@step("I input text into textbox with id \'([^\']*)\'")
def when_i_lunch_browser(step, id):
    #world.browser = webdriver.Chrome()
    element = world.browser.find_element_by_id(id)
