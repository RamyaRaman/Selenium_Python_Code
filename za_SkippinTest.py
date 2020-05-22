import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest  #decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping as its not ready")
    def test_advancedsearch(self):
        print("This is adv search method")

    @unittest.skipIf(1==1,"One not equal to one")
    def test_prepaid(self):
        print("This is prepaid")

    def test_post(self):
        print("This is postpaid")

    def test_gmail(self):
        print("Login gmail")

    def test_byTwitter(self):
        print("Login Twitter")


if __name__== "__main__":
    unittest.main()