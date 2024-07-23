class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)


# Pre-order 1 2 4 5 3
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


pre_order(tree)
print()


# Post-order 4 5 2 3 1
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


post_order(tree)
print()


# In-order 4 2 5 1 3

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


in_order(tree)
