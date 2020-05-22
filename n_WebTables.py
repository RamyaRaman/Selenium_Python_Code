from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.toolsqa.com/automation-practice-table/")

rows = len(driver.find_elements_by_xpath("//*[@id='content']/table/tbody/tr"))# counts how many ts's is there i.e the rows
cols = len(driver.find_elements_by_xpath("//*[@id='content']/table/thead/tr/th")) #count number of columns

print(rows)
print(cols)

print("Country"+"       "+"City"+"      "+"Height"+"        "+"Built"+"         "+"Rank"+"          "+"...")

for r in range(1,rows+1):
    for c in range(1,cols):
        value = driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='       ')
    print()
