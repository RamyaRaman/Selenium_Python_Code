
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with radio buttons
stat1 = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(stat1)


driver.find_element_by_id("RESULT_RadioButton-7_0").click()

stat1 = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(stat1)
# Working with checkboxes

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
