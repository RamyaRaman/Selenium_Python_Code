#Relational comparison

import unittest

class Test(unittest.TestCase):
    def testName(self):

        self.assertGreater(100,10) #True
        self.assertGreaterEqual(100,10)  #True

        self.assertLess(10, 100)  # True
        self.assertLessEqual(10, 100)  # True
if __name__ == "__main__":
    unittest.main()
