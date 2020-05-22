from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
time.sleep(3)
driver.switch_to.frame("packageListFrame") #select the first frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content() # come out of first frame

driver.switch_to.frame("packageFrame") #second frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content() # come out of second frame

driver.switch_to.frame("classFrame") #third frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)