from collections import deque

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree_bfs(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    queue = deque([tree])

    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return tree


def print_binary_tree(tree: BinaryTree, level=0):
    if tree is not None:
        print(" " * (2 * level) + str(tree.value))
        if tree.left or tree.right:
            if tree.left:
                print_binary_tree(tree.left, level + 1)
            else:
                print(" " * (2 * (level + 1)) + " ")
            if tree.right:
                print_binary_tree(tree.right, level + 1)
            else:
                print(" " * (2 * (level + 1)) + " ")
            
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Початкове бінарне дерево:")
print_binary_tree(root)

new_root = invert_binary_tree_bfs(root)

print("\nІнвертоване бінарне дерево:")
print_binary_tree(new_root)
