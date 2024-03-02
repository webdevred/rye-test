
import unittest
import numpy as np

from rs import hello_func, calc_func

class TestRyeSample(unittest.TestCase):

    def test_hello_func(self):
        hello_func()

    def test_numpy_arr_sum(self):
        arr1 = np.array([1,2])
        arr2 = np.array([5,6])
        expected = np.array([6,8])
        ret = calc_func(arr1, arr2)
        assert(np.all(ret == expected))

if __name__ == '__main__':
    unittest.main()
