import unittest, numpy

class VarianceTestCase(unittest.TestCase):

    def setUp(self):
        self.seed = int(numpy.random.randint(2**31-1))
        numpy.random.seed(self.seed)
        print 'Random seed for the tests:', self.seed

    def test_var(self):
        N, D = 100000, 5
        # goal variances: [0.1 , 0.45, 0.8 ,    1.15,  1.5]
        desired = numpy.linspace(0.1, 1.5, D)
        # test multiple times with random data
        for _ in range(20):
            # generate random, D-dimensional data
            x = numpy.random.randn(N, D) * numpy.sqrt(desired)
            variance = numpy.var(x, axis=0)
            numpy.testing.assert_array_almost_equal(
                    variance, desired, 1)
