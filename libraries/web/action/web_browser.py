__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import pdb
import sys
sys.path.append(sys.path[0] + "/../log")
import sqlite_logger


@step("I open web browser")
@sqlite_logger.logit
def i_open_browser(step):
    world.browser = webdriver.Chrome()


@step("I open page \'([^\']*)\'")
@sqlite_logger.logit
def i_open_page(step, url):
    world.browser.get(url)


@step("I close web browser")
@sqlite_logger.logit
def i_close_browser(step):
    world.browser.close()
