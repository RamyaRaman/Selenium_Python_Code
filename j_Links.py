#How many links present in the link

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

#note all the links will have a tag name as a

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links",len(links))

#extract all the links and print in the console

for link in links:
    print(link.text)

#click on the link
#driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()