import sys
sys.path.append("C:/Users/admin/Desktop/algolab7")
from src.metod import initialize_dict, find_max_chain_length
import unittest

class TestWchainFunctions(unittest.TestCase):
    def test_initialize_dict(self):
        words = ["cat", "dog", "bird", "fish"]
        expected_dict = {3: ["cat", "dog"], 4: ["bird", "fish"]}

        actual_dict = initialize_dict(words)
        self.assertEqual(expected_dict, actual_dict)

    def test_find_max_chain_length_base_case(self):
        word = "cat"
        word_dict = {"3": ["cat", "dog"]}
        storage = {}

        expected_length = 1

        actual_length = find_max_chain_length(word, word_dict, storage)
        self.assertEqual(expected_length, actual_length)

    def test_find_max_chain_length_complex_case(self):
        word = "apple"
        word_dict = {4: ["apple", "pear"], 5: ["grape", "fruit"]}
        storage = {}

        expected_length = 1

        actual_length = find_max_chain_length(word, word_dict, storage)
        self.assertEqual(expected_length, actual_length)

if __name__ == "__main__":
    unittest.main()
