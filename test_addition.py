#unit test
""" doc string"""
import unittest
from project2.addition import add

class AdditionTestCase(unittest.TestCase):
    """Tests for `addtion.py`"""

    def test_is_valid_input(self):
        """checking for input in codes"""
        self.assertFalse(add('4', '5'))
    def test_is_alphabet(self):
        """testing for alphabets"""
        self.assertFalse('A'.islower())
    def test_is_valid_input2(self):
        """testing for normal integers"""
        self.assertTrue(add(4, 5))
if __name__ == '__main__':
    unittest.main()
