__author__ = 'bob.zhu'
from lettuce import *
from selenium import webdriver
import pdb
import sys

sys.path.append(sys.path[0] + "/../decorator")
import global_decorator


@step("I open web browser")
def i_open_browser(_step):
    # pdb.set_trace()
    i_open_browser_impl(_step)


@global_decorator.logit
def i_open_browser_impl(_step):
    world.browser = webdriver.Chrome()
    world.browser.maximize_window()


@step("I open page \'([^\']*)\'")
def i_open_page(_step, url):
    i_open_page_impl(_step, url)


@global_decorator.logit
def i_open_page_impl(_step, url):
    world.browser.get(url)


@step("I close web browser")
def i_close_browser(_step):
    i_close_browser_impl(_step)


@global_decorator.logit
def i_close_browser_impl(_step):
    world.browser.close()

@step("I want sleep \'([^\']*)\' seconds")
def i_sleep_for_a_while(_step, seconds):
    seconds = int(seconds)
    import time
    time.sleep(seconds)
