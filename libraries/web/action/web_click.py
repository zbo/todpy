__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time
import sys
sys.path.append(sys.path[0] + "/../log")
import sqlite_logger


@step("I click element with class \'([^\']*)\'")
def i_click_element_with_class(step, css):
    i_click_element_with_class_impl(css)


@sqlite_logger.logit
def i_click_element_with_class_impl(css):
    element = world.browser.find_element_by_class_name(css)
    element.click()


@step("I click element with text \'([^\']*)\'")
def i_click_element_with_text(step, text):
    i_click_element_with_text_impl(text)


@sqlite_logger.logit
def i_click_element_with_text_impl(text):
    element = world.browser.find_element_by_link_text(text)
    element.click()


@step("I click element with id \'([^\']*)\'")
def i_click_element_with_id(step, id):
    i_click_element_with_id_impl(id)


@sqlite_logger.logit
def i_click_element_with_id_impl(id):
    element = world.browser.find_element_by_id(id)
    element.click()
