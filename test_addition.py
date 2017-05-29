#unit test
""" doc string"""
import unittest
from project2.addition import add

class AdditionTestCase(unittest.TestCase):
    """Tests for `addtion.py`"""

    def test_is_valid_input(self):
        """test?"""
        self.assertTrue(add(4, 5))
    def test_is_alphabet(self):
        """test?"""
        self.assertFalse('A'.islower())
    def test_is_valid_input2(self):
        """test?"""
        self.assertTrue(add(4, 5))
    def test_negative_number(self):
    """Is a negative number correctly determined not to be prime?"""
    for index in range(-1, -10, -1):
        self.assertFalse(add(index, index))
if __name__ == '__main__':
    unittest.main()
