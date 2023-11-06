import unittest
from lab import find_root

class TestFindRoot(unittest.TestCase):
    def test_no_root(self):
        graph = {1: [2], 2: [3], 3: [1]}
        result = find_root(graph)
        self.assertEqual(result, -1)

    def test_single_root(self):
        graph = {1: []} 
        result = find_root(graph)
        self.assertEqual(result, 1)


    def test_multiple_roots(self):
        graph = {1: [2], 2: [3], 4: [5]}
        result = find_root(graph)
        self.assertIn(result, [1, 4]) 


    def test_empty_graph(self):
        graph = {}
        result = find_root(graph)
        self.assertEqual(result, -1)

    def test_cyclic_graph(self):
        graph = {1: [2], 2: [3], 3: [1]}
        result = find_root(graph)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
