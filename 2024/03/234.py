# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.

import sys

sys.path.append("../..")

from ListNode import ListNode


def isPalindrome(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans == ans[::-1]


# Example 1:
head = [1, 2, 2, 1]
ans = True
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if isPalindrome(root) == ans else "Fail")

# Example 2:
head = [1, 2]
ans = False
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if isPalindrome(root) == ans else "Fail")
