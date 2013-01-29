import unittest

class LowerTestCase(unittest.TestCase):
    def test_lower(self):
        # Given
        string = 'HeLlO wOrld'
        expected = 'hello world'
        # When
        output = string.lower()
        # Then
        self.assertEqual(output, expected)
