from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com")

#driver.save_screenshot("G:\Python\homepage.png")
driver.get_screenshot_as_file("G:\Python\homepage2.png")