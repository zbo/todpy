__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time
import sys
sys.path.append(sys.path[0] + "/../decorator")
import global_decorator


@step("I see \'([^\']*)\' in the title")
def i_see_text_in_the_title(step, text):
    i_see_text_in_the_title_imple(step, text)


@global_decorator.logit
def i_see_text_in_the_title_imple(step, text):
    assert text in world.browser.title


@step("I see \'([^\']*)\' in textbox with id \'([^\']*)\'")
def i_see_text_in_textbox_with_id(step, text, id):
    i_see_text_in_textbox_with_id_impl(step, id, text)


@global_decorator.logit
def i_see_text_in_textbox_with_id_impl(step, id, text):
    element = world.browser.find_element_by_id(id)
    element.click()
    text_in = element.get_attribute('value').encode('utf-8')
    assert text == text_in
