#unit test
""" doc string"""
import unittest
from project2.addition import add

class AdditionTestCase(unittest.TestCase):
    """Tests for `addtion.py`"""

    def test_is_valid_input(self):
        """test?"""
        self.assertTrue(add(4, 5))
    def test_is_number(self):
        """test?"""
        self.assertTrue('A'.isdigit())
    def test_is_alphabet(self):
        """test?"""
        self.assertFalse('A'.islower())
    def test_is_valid_input2(self):
        """test?"""
        self.assertTrue(add(4, 5))

if __name__ == '__main__':
    unittest.main()
