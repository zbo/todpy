__author__ = 'bob.zhu'
from selenium import webdriver
import time

browser = webdriver.Chrome() #.Firefox()  # Get local session of firefox
browser.get("http://www.mi.com/en/")  # Load page
assert "Mi" in browser.title

first_tab = browser.find_element_by_class_name("nav-item")
first_tab.click()
time.sleep(2)
link = first_tab.find_elements_by_link_text("Mi Note")[0]
link.click()
assert "Note" in browser.title
browser.close()