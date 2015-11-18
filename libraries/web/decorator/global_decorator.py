__author__ = 'bob.zhu'
import pdb
import time
import traceback
from lettuce import *
from selenium import webdriver


def logit(func):
    def wrapper(*args):
        write_file(
            "{0} start @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))
        try:
            func(*args)
        except Exception,e:
            write_file(traceback.format_exc())
            world.browser.close()
            raise e
        write_file(
            "{0} end @ {1}".format(func.func_name, time.strftime('%Y-%m-%d %X %Z', time.localtime(time.time()))))
    return wrapper


def write_file(content):
    file_object = open("./log.txt", "a")
    file_object.writelines(content + "\r\n")
    file_object.close()
    pass
