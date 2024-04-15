# 129. Sum Root to Leaf Numbers
# Medium
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
import sys

sys.path.append("../..")

from TreeNode import TreeNode


"""
Input: Binary Tree
Output: Int
Solution: Recursively add up the nodes using a depth first search
"""


def sumNumbers(root):

    def dfs(node, path):
        if not node:
            return 0

        curr = path * 10 + node.val
        if not node.left and not node.right:
            return curr
        return dfs(node.left, curr) + dfs(node.right, curr)

    return dfs(root, 0)


# Example 1:
root = [1, 2, 3]
ans = 25
root = TreeNode().from_list(root)
print("Pass" if sumNumbers(root) == ans else "Fail")
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
root = [4, 9, 0, 5, 1]
ans = 1026
root = TreeNode().from_list(root)
print("Pass" if sumNumbers(root) == ans else "Fail")
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
