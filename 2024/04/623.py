# 623. Add One Row to Tree
# Medium
# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
# Note that the root node is at depth 1.
# The adding rule is :
# Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
# cur's original left subtree should be the left subtree of the new left subtree root.
# cur's original right subtree should be the right subtree of the new right subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.


import sys

sys.path.append("../..")

from TreeNode import TreeNode


def addOne(root, val, depth):
    if depth == 1:
        return TreeNode(val, root, None).to_list()

    def dfs(node, val, depth):
        if not node:
            return

        if depth <= 2:
            temp_left = node.left
            temp_right = node.right
            node.left = TreeNode(val=val, left=temp_left)
            node.right = TreeNode(val=val, right=temp_right)
            return
        dfs(node.left, val, depth - 1)
        dfs(node.right, val, depth - 1)

    dfs(root, val, depth)
    return root.to_list()


# Example 1:
arr = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2
ans = [4, 1, 1, 2, None, None, 6, 3, 1, 5]
root = TreeNode().from_list(arr)
print("Pass" if addOne(root, val, depth) == ans else "Fail")
# Example 2:
arr = [4, 2, None, 3, 1]
val = 1
depth = 3
ans = [4, 2, None, 1, 1, 3, None, None, 1]
root = TreeNode().from_list(arr)
print("Pass" if addOne(root, val, depth) == ans else "Fail")
# Example 3:
arr = [4, 2, 6, 3, 1, 5]
val = 1
depth = 1
ans = [1, 4, None, 2, 6, 3, 1, 5]
root = TreeNode().from_list(arr)
print("Pass" if addOne(root, val, depth) == ans else "Fail")
# Constraints:
# The number of nodes in the tree is in the range[1, 104].
# The depth of the tree is in the range[1, 104].
# -100 <= Node.val <= 100
# -105 <= val <= 105
# 1 <= depth <= the depth of tree + 1
