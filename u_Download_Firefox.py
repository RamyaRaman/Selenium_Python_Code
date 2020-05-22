from selenium import webdriver

#Firefox settings for pop up
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf") #Mind type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:\Downloadedfiles")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

#here add the chromeoptions=
driver = webdriver.firefox(executable_path="C:\Drivers\cgeckdriver.......",
                           firefox_profile=fp)
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