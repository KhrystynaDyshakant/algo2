import unittest

from possible_num_of_pairs import possible_num_of_pairs

class TestPossibleNumOfPairs(unittest.TestCase):

       def test_count_of_pairs(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 4)

       def test_count_of_pairs_second(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 6)

       def test_count_of_pairs_with_even_numbers(self):
        pairs = [(2, 4), (6, 8), (10, 12), (14, 16)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 0)

       def test_count_of_pairs_with_odd_numbers(self):
        pairs = [(3, 5), (7, 9), (11, 13), (15, 17)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()