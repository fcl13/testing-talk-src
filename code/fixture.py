import unittest

class FirstTestCase(unittest.TestCase):
    def setUp(self):
        """setUp is called before every test"""
        pass
    def tearDown(self):
        """tearDown is called at the end of every test"""
        pass
    @classmethod
    def setUpClass(cls):
        """Called once before all tests in this class."""
        pass
    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class."""
        pass
    # ... all tests here ...
