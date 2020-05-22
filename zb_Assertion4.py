#assertIn and AssertNotIn

import unittest

class Test(unittest.TestCase):

    def testName(self):
        list = ("python","selenium","java")
        self.assertIn("python",list) #True
        self.assertNotIn("python",list) #Fail

if __name__ == "__main__":
    unittest.main()
