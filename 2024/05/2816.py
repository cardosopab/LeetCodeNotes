# 2816. Double a Number Represented as a Linked List
# Medium
# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

import sys

sys.path.append("../..")

from ListNode import ListNode
from collections import deque


class Solution:
    def doubleIt(self, head):
        num = 0

        while head:
            num = num * 10 + head.val
            head = head.next

        num *= 2
        q = deque()

        while num > 0:
            q.appendleft(num % 10)
            num //= 10

        new_head = ListNode(-1)
        dummy = new_head

        for n in q:
            dummy.next = ListNode(n)
            dummy = dummy.next

        return ListNode().linkedListToArray(new_head.next)


# Example 1:
head = [1, 8, 9]
ans = [3, 7, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().doubleIt(root)
print("Pass" if res == ans else f"Fail: {res}")
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

# Example 2:
head = [9, 9, 9]
ans = [1, 9, 9, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().doubleIt(root)
print("Pass" if res == ans else f"Fail: {res}")
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

# Constraints:
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.


class Solution:
    def doubleIt(self, head):
        dummy = self.reverseList(head)
        new_head = ListNode(-1)
        tail = new_head
        carry = 0

        while dummy:
            end = (dummy.val * 2 + carry) % 10
            carry = (dummy.val * 2) // 10
            tail.next = ListNode(end)
            tail = tail.next
            dummy = dummy.next

        if carry:
            tail.next = ListNode(carry)
            tail = tail.next

        return ListNode().linkedListToArray(self.reverseList(new_head.next))

    def reverseList(self, node):
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev


# Example 1:
head = [1, 8, 9]
ans = [3, 7, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().doubleIt(root)
print("Pass" if res == ans else f"Fail: {res}")

# Example 2:
head = [9, 9, 9]
ans = [1, 9, 9, 8]
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().doubleIt(root)
print("Pass" if res == ans else f"Fail: {res}")
