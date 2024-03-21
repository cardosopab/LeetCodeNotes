# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: ListNode
# Output: ListNode
# Solution: Consider swapping the liquids between cup A and B, it's simple if you have a third cup.
import sys

sys.path.append("../..")
from ListNode import ListNode


def reverseList(root):
    curr = root
    prev = None

    while curr:
        # Temp cup
        temp = curr.next
        # Cup A
        curr.next = prev
        # Cup B
        prev = curr
        # Continue forward
        curr = temp
    ans = ListNode().linkedListToArray(prev)
    return ans


# Example 1:
head = [1, 2, 3, 4, 5]
ans = [5, 4, 3, 2, 1]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reverseList(root) == ans else "Fail")
# Example 2:
head = [1, 2]
ans = [2, 1]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reverseList(root) == ans else "Fail")
# Example 3:
head = []
ans = []
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reverseList(root) == ans else "Fail")
