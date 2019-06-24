"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest


class AssertDemo(unittest.TestCase):
    def test_asserTrueFalse(self):
        a = True;
        self.assertTrue(a, "a is not True")
        b = True
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Test"
        b = "test"
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)