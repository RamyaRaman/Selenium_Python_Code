from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

#Capture all cookinf created by browser
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookie pairs

# Adding new cookie to the browser
cooki = {'name': 'MyCookie','value':'1234567890'}
driver.add_cookie(cooki)
#now again find all the cookies to see if new cookie is displaying
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies after adding
print(cookies) #print all the cookie pairs

# Deleting cookie
driver.delete_cookie("MyCookie")

#now again find all the cookies to see if new cookie is deleted
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies after deleting
print(cookies) #print all the cookie pairs

#Delete all the cookies
driver.delete_all_cookies() #deletes all cookies
cookies = driver.get_cookies()
print(len(cookies))


