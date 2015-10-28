__author__ = 'bob.zhu'

from lettuce import *
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

@step("I lunch app in device")
def i_lunch_app_in_device(step):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = '192.168.56.111:5555'
    desired_caps['app'] = PATH(
        '../../../sample-code/apps/ContactManager/ContactManager.apk'
    )
    desired_caps['appPackage'] = 'com.example.android.contactmanager'
    desired_caps['appActivity'] = '.ContactManager'
    world.driver=driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps);
    pass


@step("I quit app")
def i_quit_app(step):
    pass
