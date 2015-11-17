__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import pdb
import sys

sys.path.append(sys.path[0] + "/../decorator")
import global_decorator


@step("I open web browser")
def i_open_browser(step):
    i_open_browser_impl()


@global_decorator.logit
def i_open_browser_impl():
    world.browser = webdriver.Chrome()


@step("I open page \'([^\']*)\'")
def i_open_page(step, url):
    i_open_page_impl(url)


@global_decorator.logit
def i_open_page_impl(url):
    world.browser.get(url)


@step("I close web browser")
def i_close_browser(step):
    i_close_browser_imple()


@global_decorator.logit
def i_close_browser_imple():
    world.browser.close()
