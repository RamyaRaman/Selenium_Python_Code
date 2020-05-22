import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebpage = driver.title

        #assertEqual
        self.assertEqual("Google",titleOfWebpage,"webpage title is not same")
            #OR
        self.assertNotEqual("Google123",titleOfWebpage)
if __name__ == "__main__":
    unittest.main()
