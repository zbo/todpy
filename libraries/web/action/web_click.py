__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time


@step("I click element with class \'([^\']*)\'")
def i_click_element_with_class(step, css):
    element = world.browser.find_element_by_class_name(css)
    element.click()


@step("I click element with text \'([^\']*)\'")
def i_click_element_with_text(step, text):
    element = world.browser.find_element_by_link_text(text)
    element.click()


@step("I click element with id \'([^\']*)\'")
def when_i_click_element_with_id_group1(step, id):
    element = world.browser.find_element_by_id(id)
    element.click()
