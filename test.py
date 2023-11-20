import unittest

from possible_num_of_pairs import possible_num_of_pairs

class TestPossibleNumOfPairs(unittest.TestCase):

    def test_empty_input(self):
        pairs = []
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 0)

    def test_single_boy_girl_pair(self):
        pairs = [(1, 2)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 1)

    def test_multiple_boys_girls_same_tribe(self):
        pairs = [(1, 2), (3, 4), (5, 6)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 9)

    def test_multiple_boys_girls_different_tribes(self):
        pairs = [(1, 2), (2, 4), (3, 5), (8, 10)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 6)

    def test_repeated_pairs(self):
        pairs = [(1, 2), (2, 4), (1, 2), (2, 4), (3, 5), (3, 5), (8, 10)]
        result = possible_num_of_pairs(pairs)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()