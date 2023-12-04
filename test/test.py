import sys
sys.path.append("C:/Users/admin/Desktop/algo6lab")
from src.naive_metod import naive_method
import unittest


class TestNaiveMethod(unittest.TestCase):

    def test_empty_needle(self):
        haystack = "abcdef"
        needle = ""
        result, comparisons = naive_method(haystack, needle)
        self.assertEqual(-1, result)
        self.assertEqual(0, comparisons)

    def test_needle_not_in_haystack(self):
        haystack = "abcdef"
        needle = "xyz"
        result, comparisons = naive_method(haystack, needle)
        self.assertEqual(-1, result)
        self.assertEqual(len(haystack) - len(needle) + 1, comparisons)

    def test_needle_at_beginning(self):
        haystack = "abcdef"
        needle = "abc"
        result, comparisons = naive_method(haystack, needle)
        self.assertEqual(result, 0)
        self.assertEqual(comparisons, len(haystack))

    def test_needle_at_end(self):
        haystack = "abcdef"
        needle = "def"
        result, comparisons = naive_method(haystack, needle)
        self.assertEqual(3, result)
        self.assertEqual(comparisons, len(haystack))

    def test_needle_multiple_occurrences(self):
        haystack = "abracadabra"
        needle = "abra"
        result, comparisons = naive_method(haystack, needle)
        self.assertEqual(result, 7)
        self.assertLess(len(haystack), comparisons)


if __name__ == '__main__':
    unittest.main()