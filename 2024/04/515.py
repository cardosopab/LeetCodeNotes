# 515. Find Largest Value in Each Tree Row
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).


import sys

sys.path.append("../..")

from TreeNode import TreeNode
from collections import deque


def largestValues(root):
    d = deque([root])
    res = []

    while d:
        max_n = float("-inf")
        lvl_size = len(d)
        for _ in range(lvl_size):
            node = d.popleft()
            max_n = max(max_n, node.val)
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        res.append(max_n)

    return res


# Example 1:
root = [1, 3, 2, 5, 3, None, 9]
ans = [1, 3, 9]
root = TreeNode.from_list(root)
res = largestValues(root)
# print(res)
print("Pass" if res == ans else "Fail")

# Example 2:
root = [1, 2, 3]
ans = [1, 3]
root = TreeNode.from_list(root)
res = largestValues(root)
# print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1
