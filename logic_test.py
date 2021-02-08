import unittest
from logic import wd_sum

class TestStringMethods(unittest.TestCase):

    def test_valid_sum_int(self):
        result = wd_sum(1, 2)
        self.assertEqual(result, 3)

    def test_exception(self):
        # check that wd_sum
        with self.assertRaises(Exception):
            wd_sum(1, None)

if __name__ == '__main__':
    unittest.main()