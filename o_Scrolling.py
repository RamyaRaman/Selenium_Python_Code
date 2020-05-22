from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() #maximize thr window

#1. Scroll using pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#2. Scroll until u find elemeent
#flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[91]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#3. Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

