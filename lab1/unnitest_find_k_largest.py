import unittest
from find_k_largest import find_k_largest

class TestFindKLargest(unittest.TestCase):
    def test_1(self):
        nums = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        result, index = find_k_largest(nums, k)
        self.assertEqual(result, 22)
        self.assertEqual(index, 2)

    def test_2(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        result, index = find_k_largest(nums, k)
        self.assertEqual(result, 5)
        self.assertEqual(index, 0)

    def test_3(self):
        nums = [1, 1, 1, 1, 1]
        k = 1
        result, index = find_k_largest(nums, k)
        self.assertEqual(result, 1)
        self.assertEqual(index, 0)

if __name__ == '__main__':
    unittest.main()

