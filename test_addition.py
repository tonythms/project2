#unit test
""" doc string"""
import unittest
from project2.addition import add

class AdditionTestCase(unittest.TestCase):
    """Tests for `addtion.py`"""

    def test_is_valid_input(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(add(2, 4))

if __name__ == '__main__':
    unittest.main()
