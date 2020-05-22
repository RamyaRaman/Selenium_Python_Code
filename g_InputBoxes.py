from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# The below 3 we can find.
#1. How to find how many inputboxes present in web page
#2. How to provide value into text box
#3. How to get the status


#1. How to find how many inputboxes present in web page

inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

#2. How to provide value into text box
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Dolly")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Dora")
driver.find_element_by_id('RESULT_TextField-3').send_keys("123654789")

#3. How to get the status

sta1 = driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(sta1)









