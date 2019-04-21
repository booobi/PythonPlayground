import unittest
import bisection_method


class tests(unittest.TestCase):
    def test_input_function(self):
        self.assertEquals(bisection_method.f(1), -1, "Function value for " + str(1))

    def test_invalid_function_values(self):
        self.assertRaises(Exception, bisection_method.bisection, bisection_method.f, 2, 2, 0.0001, 1000)
