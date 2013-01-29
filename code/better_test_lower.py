import unittest

class LowerTestCase(unittest.TestCase):
    def test_lower(self):
        # Given
        # Each test case is a tuple of (input, expected_result)
        test_cases = [('HeLlO wOrld', 'hello world'),
                      ('hi', 'hi'),
                      ('123 ([?', '123 ([?'),
                      ('', '')]
        for string, expected in test_cases:
            # When
            output = string.lower()
            # Then
            self.assertEqual(output, expected)
