import unittest

def setUpModule(): # will be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule(): # will be executed after completing everthing present in the python module
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    # Execute before all the test methods
    def setUp(self):  # like a pre-requisite
        print("This is login test")

    # Execute after all the test methods
    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #Execute once the class is started
        print("Open Application")

    @classmethod
    def tearDownClass(cls): #Execute once the class is completed
        print("Close App")

    def test_search(self):
        print("Search test")

    def test_adsearch(self):
        print("Advance Search test")

    def test_prepaidRecharge(self):
        print("PrepaidRecharge test")

    def test_postpaidRecharge(self):
        print("PostpaidRecharge test")


if __name__=="__main__":
    unittest.main()