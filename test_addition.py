#unit test
""" doc string"""
import unittest
from addition import add
A='7'
B='5'
C='0'
D='0'
class AdditionTestCase(unittest.TestCase):
    """Tests for `addtion.py`"""

    def test_is_valid_input(self):
        """checking for input in codes"""
        self.assertTrue(add(A, B))
    def test_is_valid_input(self):
        """checking for input in codes"""
        self.assertTrue(add(A, C))  
    def test_is_alphabetl(self):
        """testing for alphabets"""
        self.assertFalse(A.islower())
    def test_is_valid_input2(self):
        """testing for normal integers"""
        self.assertFalse(add(C, D))
    def test_is_alphabetu(self):
        """testing for digits"""
        self.assertTrue(A.isdigit())
if __name__ == '__main__':
    unittest.main()
