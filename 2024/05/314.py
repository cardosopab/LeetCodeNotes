# 314. Binary Tree Vertical Order Traversal
# Description
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

import sys

sys.path.append("../..")

from TreeNode import TreeNode
from collections import defaultdict, deque


def vertical_traverse(root):
    q = deque([(root, 0)])
    d = defaultdict(list)

    while q:
        for _ in range(len(q)):
            node, offset = q.popleft()
            d[offset].append(node.val)

            if node.left:
                q.append((node.left, offset - 1))
            if node.right:
                q.append((node.right, offset + 1))

    return [v for _, v in sorted(d.items())]


null = None
# Example 1:
root = [3, 9, 20, null, null, 15, 7]
ans = [[9], [3, 15], [20], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")

# Example 2:
root = [3, 9, 8, 4, 0, 1, 7]
ans = [[4], [9], [3, 0, 1], [8], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")

# Example 3:
root = [3, 9, 8, 4, 0, 1, 7, null, null, null, 2, 5]
ans = [[4], [9, 5], [3, 0, 1], [8, 2], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")


# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


def vertical_traverse(root):
    q = deque([(root, 0)])
    d = defaultdict(list)
    min_idx = float("inf")
    max_idx = float("-inf")

    while q:
        for _ in range(len(q)):
            node, offset = q.popleft()

            min_idx = min(min_idx, offset)
            max_idx = max(max_idx, offset)

            d[offset].append(node.val)

            if node.left:
                q.append((node.left, offset - 1))
            if node.right:
                q.append((node.right, offset + 1))

    ans = []
    for i in range(min_idx, max_idx + 1):
        ans.append(d[i])

    return ans


# Example 1:
root = [3, 9, 20, null, null, 15, 7]
ans = [[9], [3, 15], [20], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")

# Example 2:
root = [3, 9, 8, 4, 0, 1, 7]
ans = [[4], [9], [3, 0, 1], [8], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")

# Example 3:
root = [3, 9, 8, 4, 0, 1, 7, null, null, null, 2, 5]
ans = [[4], [9, 5], [3, 0, 1], [8, 2], [7]]
root = TreeNode().from_list(root)
res = vertical_traverse(root)
print("Pass" if res == ans else f"Fail: {res}")
