import unittest
from binaryTree import invert_binary_tree_bfs
from binaryTree import BinaryTree


class TestBinaryTreeInversion(unittest.TestCase):

    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_root = invert_binary_tree_bfs(root)

        self.assertEqual(inverted_root.value, 1)
        self.assertEqual(inverted_root.left.value, 3)
        self.assertEqual(inverted_root.right.value, 2)
        self.assertEqual(inverted_root.left.left.value, 7)
        self.assertEqual(inverted_root.left.right.value, 6)
        self.assertEqual(inverted_root.right.left.value, 5)
        self.assertEqual(inverted_root.right.right.value, 4)

    def test_invert_binary_tree_(self):

        root = None
        inverted_root = invert_binary_tree_bfs(root)

        self.assertEqual(inverted_root, None)

if __name__ == '__main__':
    unittest.main()
