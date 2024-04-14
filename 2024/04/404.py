# 404. Sum of Left Leaves
# Easy
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
import sys

sys.path.append("../..")

from TreeNode import TreeNode


def sumOfLeftLeaves(root):
    def dfs(node, is_left):
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val if is_left else 0

        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)


# Example 1:
arr = [3, 9, 20, None, None, 15, 7]
ans = 24
root = TreeNode().from_list(arr)
print("Pass" if sumOfLeftLeaves(root) == ans else "Fail")
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:
arr = [1]
ans = 0
root = TreeNode().from_list(arr)
print("Pass" if sumOfLeftLeaves(root) == ans else "Fail")
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
