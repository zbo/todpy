__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time

@step("I see the \'([^\']*)\' in the title")
def then_i_see_the_group1_in_the_title(step, text):
    assert text in world.browser.title

@step("I see the \'([^\']*)\' in the title")
def then_i_see_the_group1_in_the_title(step, text):
    assert text in world.browser.title