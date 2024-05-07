# 92. Reverse Linked List II
# Medium
# Topics
# Companies
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


import sys

sys.path.append("../..")

from ListNode import ListNode


class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(-1, head)

        left_prev, curr = dummy, head
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left_prev.next.next = curr
        left_prev.next = prev

        return ListNode().linkedListToArray(head)


# Example 1:
head = [1, 2, 3, 4, 5]
left = 2
right = 4
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().reverseBetween(root, left, right)
ans = [1, 4, 3, 2, 5]
print("Pass" if res == ans else f"Fail: {res}")

# Example 2:
head = [5]
left = 1
right = 1
root = ListNode().arrayToLinkedList(head, len(head))
res = Solution().reverseBetween(root, left, right)
ans = [5]
print("Pass" if res == ans else f"Fail: {res}")

# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Follow up: Could you do it in one pass?
