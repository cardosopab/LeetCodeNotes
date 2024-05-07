# 2487. Remove Nodes From Linked List
# Medium
# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.


import sys

sys.path.append("../..")

from ListNode import ListNode


class Solution:
    def removeNodes(self, head):
        return ListNode().linkedListToArray(
            self.reverseList(self.monoIncrease(self.reverseList(head)))
        )

    def monoIncrease(self, node):
        curr = node

        while curr:
            while curr.next and curr.val > curr.next.val:
                curr.next = curr.next.next
            if curr:
                curr = curr.next
            else:
                break

        return node

    def reverseList(self, node):
        curr = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# Example 1:
head = [5, 2, 13, 3, 8]
ans = [13, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:
head = [1, 1, 1, 1]
ans = [1, 1, 1, 1]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")
# Explanation: Every node has value 1, so no nodes are removed.

# Constraints:
# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105


class Solution:
    def removeNodes(self, head):
        curr = head
        stack = []

        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        curr = dummy
        for n in stack:
            curr.next = ListNode(n)
            curr = curr.next

        return ListNode().linkedListToArray(dummy.next)


# Example 1:
head = [5, 2, 13, 3, 8]
ans = [13, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")

# Example 2:
head = [1, 1, 1, 1]
ans = [1, 1, 1, 1]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")


class Solution:
    def removeNodes(self, head):
        slow = dummy = head
        while slow:
            fast = slow
            curr_max = slow.val
            while fast:
                curr_max = max(curr_max, fast.val)
                fast = fast.next
            while slow and slow.next and slow.val < curr_max:
                slow.val = slow.next.val
                slow.next = slow.next.next
            slow = slow.next

        return ListNode().linkedListToArray(dummy)


# Example 1:
head = [5, 2, 13, 3, 8]
ans = [13, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")

# Example 2:
head = [1, 1, 1, 1]
ans = [1, 1, 1, 1]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().removeNodes(root)
print(f"Pass: {res}" if ans == res else f"Fail: {res}")
