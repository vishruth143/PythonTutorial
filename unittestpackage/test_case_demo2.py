import unittest


class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run once before every tests")

    def setUp(self):
        print("I will run before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run once after every tests")


if __name__ == '__main__':
    unittest.main(verbosity=2)