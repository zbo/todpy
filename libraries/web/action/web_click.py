__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time
import pdb
import sys
sys.path.append(sys.path[0] + "/../decorator")
import global_decorator


@step("I click element with class \'([^\']*)\'")
def i_click_element_with_class(_step, css):
    i_click_element_with_class_impl(_step, css)


@global_decorator.logit
def i_click_element_with_class_impl(_step, css):
    element = world.browser.find_element_by_class_name(css)
    element.click()


@step("I click element with text \'([^\']*)\'")
def i_click_element_with_text(_step, text):
    i_click_element_with_text_impl(_step, text)


@global_decorator.logit
def i_click_element_with_text_impl(_step, text):
    element = world.browser.find_element_by_link_text(text)
    element.click()


@step("I click element with id \'([^\']*)\'")
def i_click_element_with_id(_step, id):
    i_click_element_with_id_impl(_step, id)


@global_decorator.logit
def i_click_element_with_id_impl(step, id):
    element = world.browser.find_element_by_id(id)
    element.click()
