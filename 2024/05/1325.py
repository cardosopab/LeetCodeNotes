# 1325. Delete Leaves With a Given Value
# Medium
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).


import sys

sys.path.append("../..")
from TreeNode import TreeNode


class Solution:
    def removeLeafNodes(self, root, target):
        def dfs(node, target):
            if not node:
                return

            node.left = dfs(node.left, target)
            node.right = dfs(node.right, target)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        dfs(root, target)
        return root.to_list()


# Example 1:
null = None
root = [1, 2, 3, 2, null, 2, 4]
target = 2
ans = [1, null, 3, null, 4]
root = TreeNode().from_list(root)
res = Solution().removeLeafNodes(root, target)
print("Pass" if res == ans else f"Fail: {res}")
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

# Example 2:
root = [1, 3, 3, 3, 2]
target = 3
ans = [1, 3, null, null, 2]
root = TreeNode().from_list(root)
res = Solution().removeLeafNodes(root, target)
print("Pass" if res == ans else f"Fail: {res}")

# Example 3:
root = [1, 2, null, 2, null, 2]
target = 2
ans = [1]
root = TreeNode().from_list(root)
res = Solution().removeLeafNodes(root, target)
print("Pass" if res == ans else f"Fail: {res}")
# Explanation: Leaf nodes in green with value (target = 2) are removed at each step.


# Constraints:
# The number of nodes in the tree is in the range [1, 3000].
# 1 <= Node.val
# target <= 1000
