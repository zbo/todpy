__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time


@step("I lunch web")
def when_i_lunch_browser(step):
    world.browser = webdriver.Chrome()


@step("I open page \'([^\']*)\'")
def when_i_open_page(step, url):
    world.browser.get(url)


@step("I close the web")
def when_i_close_browser(step):
    world.browser.close()
