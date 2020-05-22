# explicit wait is based on condition and not on time. but implicit uses based on time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")
#driver.find_element_by_id === this can be wrtten in different way as below
driver.find_element(By.ID,"tab-flight-tab-hp").click() #CLicks on flights button

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2) #from python
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/22/2019")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("12/24/2019")

#searches
driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

#now we create a explicit wait

#Explicit waits
wait = WebDriverWait(driver,10)
# this is the expected conditions
#EC is avaliable on webdriver page based on the requirement we can choose
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()
