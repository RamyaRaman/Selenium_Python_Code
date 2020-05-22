import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        #assertIsNone
        driver = None
        self.assertIsNone(driver) #True
            #OR
        #assertIsNotNone
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.assertIsNotNone(driver)  # True
if __name__ == "__main__":
    unittest.main()
