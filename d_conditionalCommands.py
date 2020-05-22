from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com") #FR

# validate username
user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #if its displayed
print(user_ele.is_enabled()) #return if enabled

# same thing as above can be done for password
pass_ele = driver.find_element_by_name("password")
print(pass_ele.is_displayed()) #if its displayed
print(pass_ele.is_enabled()) #return if enabled

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

driver.find_element_by_name("login").click()
rt_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(rt_radio.is_selected())

ot_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one trip",ot_radio.is_selected())