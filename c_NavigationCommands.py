from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com") #FR
print(driver.title)
driver.get("http://demo.automationtesting.in/Windows.html") #testing URL
time.sleep(5)
print(driver.title)
driver.back()

time.sleep(5)
print(driver.title)


driver.forward()
time.sleep(5)
print(driver.title)