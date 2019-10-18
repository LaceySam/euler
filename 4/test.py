import unittest

from main import is_palindrome


class TestPalindromeDetector(unittest.TestCase):

    def test_1001(self):
        self.assertTrue(is_palindrome(1111))

    def test_10001(self):
        self.assertTrue(is_palindrome(11111))

    def test_1245(self):
        self.assertFalse(is_palindrome(1245))

    def test_12345(self):
        self.assertFalse(is_palindrome(12345))


if __name__ == '__main__':
    unittest.main()
