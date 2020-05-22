from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# For chrome
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com")
print(driver.title)  # Title
print(driver.current_url) #returns the URL of the page
print(driver.page_source) #HTML code for the page
driver.close()



# For IE
driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.7.0\IEDriverServer")
driver.get("http://newtours.demoaut.com")
print(driver.title)  # Title
print(driver.current_url) #returns the URL of the page
print(driver.page_source) #HTML code for the page
driver.close()