import unittest, numpy

class NumpyTestCase(unittest.TestCase):

    def test_equality(self):
        a = numpy.array([1, 2])
        b = numpy.array([1, 2])
        self.assertEqual(a, b)
