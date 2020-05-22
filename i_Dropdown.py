
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

#1. select one option
#select by visible text
drp.select_by_visible_text("Morning")

#select by index
drp.select_by_index(2)

#select by value
drp.select_by_value("Radio-2")

#3.count how many options present
print(len(drp.options))

#2.capture options from drop down - capture all the options and print them in output
#capture all the options and print them as output

all_options = drp.options

for options in all_options:
    print(options.text)

