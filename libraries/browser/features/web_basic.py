__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import time


@step("I lunch browser")
def when_i_lunch_browser(step):
    world.browser = webdriver.Chrome()


@step("I open page \'([^\']*)\'")
def when_i_open_page(step, url):
    world.browser.get(url)


@step("I click element with class \'([^\']*)\'")
def when_i_click_element_with_class(step, css):
    element = world.browser.find_element_by_class_name(css)
    element.click()
    time.sleep(2)


@step("I click element with text \'([^\']*)\'")
def when_i_click_element_with_text(step, text):
    link = world.browser.find_elements_by_link_text("Mi Note")[0]
    link.click()
    time.sleep(2)


@step("I see the \'([^\']*)\' in the title")
def then_i_see_the_group1_in_the_title(step, text):
    assert text in world.browser.title


@step("I close the browser")
def when_i_close_browser(step):
    world.browser.close()
