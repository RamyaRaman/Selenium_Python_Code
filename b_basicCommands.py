from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #return title
print(driver.current_url) # returns the url
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close()  #closes one broswer
driver.quit() #closes all the browsers