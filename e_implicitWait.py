from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com") #FR

#for synchronization problem. ie when the application is slow we can pause the code

# implicit Applicable for all element in the page and only one time in the begining
# of the code its specified
driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()