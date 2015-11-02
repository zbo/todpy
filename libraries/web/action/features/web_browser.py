__author__ = 'bob.zhu'

from lettuce import *
from selenium import webdriver
import time


@step("I open web browser")
def i_open_browser(step):
    world.browser = webdriver.Chrome()


@step("I open page \'([^\']*)\'")
def i_open_page(step, url):
    world.browser.get(url)


@step("I close web browser")
def i_close_browser(step):
    world.browser.close()
