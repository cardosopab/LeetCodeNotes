from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr):
        if not arr:
            return None

        nodes = [None if val is None else cls(val) for val in arr]
        root = nodes[0]
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()
            if node:
                node.left = nodes[i]
                i += 1
                if i < len(arr):
                    node.right = nodes[i]
                    i += 1
                queue.extend([node.left, node.right])

        return root
