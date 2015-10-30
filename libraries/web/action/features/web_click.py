__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time


@step("I click element with class \'([^\']*)\'")
def when_i_click_element_with_class(step, css):
    element = world.browser.find_element_by_class_name(css)
    element.click()
    time.sleep(2)


@step("I click element with text \'([^\']*)\'")
def when_i_click_element_with_text(step, text):
    element = world.browser.find_elements_by_link_text(text)[0]
    element.click()
    time.sleep(2)



