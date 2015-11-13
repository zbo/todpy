__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import pdb
import sys
sys.path.append(sys.path[0] + "/../log")
import sqlite_logger

@sqlite_logger.logit
@step("I open web browser")
def i_open_browser(step):
    world.browser = webdriver.Chrome()


@sqlite_logger.logit
@step("I open page \'([^\']*)\'")
def i_open_page(step, url):
    world.browser.get(url)

@sqlite_logger.logit
@step("I close web browser")
def i_close_browser(step):
    world.browser.close()
