__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time


@step("I see \'([^\']*)\' in the title")
def i_see_text_in_the_title(step, text):
    assert text in world.browser.title


@step("I see \'([^\']*)\' in textbox with id \'([^\']*)\'")
def i_see_text_in_textbox_with_id(step, text, id):
    element = world.browser.find_element_by_id(id)
    element.click()
    text_in = element.get_attribute('value').encode('utf-8')
    assert text == text_in
