# 988. Smallest String Starting From Leaf
# Medium
# You are given the root of a binary tree where each node has a value in the range[0, 25] representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller.
# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.


import sys

sys.path.append("../..")

from TreeNode import TreeNode


def smallestFromLeaf(root):
    best = chr(ord("z") + 1)
    orda = ord("a")

    def dfs(node, curr):
        if not node:
            return

        curr.append(node.val)
        is_leaf = not node.left and not node.right
        if is_leaf:
            nonlocal best
            best = min(best, "".join(reversed(list(chr(x + orda) for x in curr))))
            return

        dfs(node.left, curr)
        if curr and node.left:
            curr.pop()
        dfs(node.right, curr)
        if curr and node.right:
            curr.pop()

    dfs(root, [])

    return best


# Example 1:
root = [0, 1, 2, 3, 4, 3, 4]
ans = "dba"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 2:
root = [25, 1, 3, 1, 3, 0, 2]
ans = "adz"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 3:
root = [2, 2, 1, None, 1, 0, None, 0]
ans = "abc"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 4:
root = [20, 7, 12, 15]
ans = "mu"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Constraints:
# The number of nodes in the tree is in the range[1, 8500].
# 0 <= Node.val <= 25


def smallestFromLeaf(root):
    table = [chr(ord("a") + i) for i in range(26)]

    def dfs(node, curr):
        if not node:
            return curr

        if not node.left:
            return dfs(node.right, table[node.val] + curr)
        if not node.right:
            return dfs(node.left, table[node.val] + curr)

        left = dfs(node.left, table[node.val] + curr)
        right = dfs(node.right, table[node.val] + curr)
        return min(left, right)

    ans = dfs(root, "")
    return ans


# Example 1:
root = [0, 1, 2, 3, 4, 3, 4]
ans = "dba"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 2:
root = [25, 1, 3, 1, 3, 0, 2]
ans = "adz"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 3:
root = [2, 2, 1, None, 1, 0, None, 0]
ans = "abc"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 4:
root = [20, 7, 12, 15]
ans = "mu"
root = TreeNode.from_list(root)
# print("Pass" if smallestFromLeaf(root) == ans else "Fail")


def smallestFromLeaf(root):
    orda = ord("a")

    def dfs(node, curr):
        if not node:
            return []

        curr.append(chr(orda + node.val))
        if not node.left and not node.right:
            return curr[::-1]

        left = dfs(node.left, curr[:])
        right = dfs(node.right, curr[:])

        if left and right:
            return min(left, right)
        elif left:
            return left
        else:
            return right

    ans = dfs(root, [])
    return "".join(ans)


# Example 1:
root = [0, 1, 2, 3, 4, 3, 4]
ans = "dba"
root = TreeNode.from_list(root)
print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 2:
root = [25, 1, 3, 1, 3, 0, 2]
ans = "adz"
root = TreeNode.from_list(root)
print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 3:
root = [2, 2, 1, None, 1, 0, None, 0]
ans = "abc"
root = TreeNode.from_list(root)
print("Pass" if smallestFromLeaf(root) == ans else "Fail")
# Example 4:
root = [20, 7, 12, 15]
ans = "mu"
root = TreeNode.from_list(root)
print("Pass" if smallestFromLeaf(root) == ans else "Fail")
