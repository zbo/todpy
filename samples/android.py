__author__ = 'bob.zhu'
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = 'e7029708'
desired_caps['appPackage'] = 'com.ringcentral.android'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['appActivity'] = '.LoginScreen'
desired_caps['app'] = 'E:/dev/dev-code/learning/appiumPy/apps/RCMobile_7.5.0.1.125_XIA_UP_Automation.apk'
driver = None
try:
    driver = webdriver.Remote('http://localhost:4730/wd/hub', desired_caps)
    time.sleep(5)
    # first login
    driver.find_element_by_id('com.ringcentral.android:id/phone').send_keys('18559730001')
    driver.find_element_by_id('com.ringcentral.android:id/password').send_keys('Test!123')
    driver.find_element_by_id('com.ringcentral.android:id/btnSignIn').click()
    time.sleep(10)
    driver.find_element_by_id('android:id/button1').click()
    driver.find_element_by_id('android:id/button1').click()
    driver.find_element_by_id('com.ringcentral.android:id/whats_new_button_left').click()
    driver.find_element_by_id('com.ringcentral.android:id/username_edit').send_keys('123456789')
    driver.find_element_by_id('com.ringcentral.android:id/saveBtn').click()
    # clean tips
    driver.find_element_by_id('com.ringcentral.android:id/btnClose').click()
    driver.find_element_by_id('com.ringcentral.android:id/title_layout').click()
    driver.back()
    driver.find_element_by_id('com.ringcentral.android:id/layout_plus').click()
    driver.back()
    driver.find_element_by_id('com.ringcentral.android:id/title_bar_photo').click()
    time.sleep(1)
    driver.find_element_by_id('com.ringcentral.android:id/btnClose').click()
    driver.back()
except Exception, err:
    print err
finally:
    if driver is not None:
        driver.quit()
