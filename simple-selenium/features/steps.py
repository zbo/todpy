__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time
import pdb


@step("I open page \'([^\']*)\'")
def i_open_page(step, url):
    # pdb.set_trace()
    world.browser = webdriver.Chrome()
    world.browser.get(url)

@step("I click element with class \'([^\']*)\'")
def i_click_element_with_class(step,css):
    # pdb.set_trace()
    world.first_tab = world.browser.find_element_by_class_name(css)
    world.first_tab.click()
    time.sleep(2)

@step("I click element with text \'([^\']*)\'")
def i_click_element_with_text(step,text):
    link = world.first_tab.find_elements_by_link_text("Mi Note")[0]
    link.click()

@step("I see the \'([^\']*)\' in the title")
def i_see_the_group1_in_the_title(step, text):
    assert text in world.browser.title
    world.browser.close()



