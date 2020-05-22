from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#specify the place where the download has to happen
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",("download.default_directory": "C:\Downloadedfiles"))

#here add the chromeoptions=
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",chrome_options=chromeOptions)
driver.get("https://testautomationpractice.blogspot.com/FileDownload.html")
driver.maximize_window()

#Download a text file

#text file download
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click() #generate file button
driver.find_element_by_id("link-to-download").click()

#download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing_pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

#driver.close()