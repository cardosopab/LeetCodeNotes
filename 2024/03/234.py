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


# Solutions in O(n) time & O(1) space:


def isPalindrome(head):
    dummy1 = head
    dummy2 = head
    prev = None
    length = 0

    # Get length
    while dummy1:
        length += 1
        dummy1 = dummy1.next

    # Cut in half
    half = length // 2
    for _ in range(half):
        dummy2 = dummy2.next

    # Reverse half
    while dummy2:
        nxt = dummy2.next
        dummy2.next = prev
        prev = dummy2
        dummy2 = nxt

    # Compare
    dummy1 = head
    while dummy1 and prev:
        if dummy1.val != prev.val:
            return False
        dummy1 = dummy1.next
        prev = prev.next

    return True


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


def isPalindrome(head):
    slow, fast, prev = head, head, None

    # Find the middle with slow and fast pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse remaining of list
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Compare slow and prev
    slow = head
    while slow and prev:
        if slow.val != prev.val:
            return False
        slow = slow.next
        prev = prev.next

    return True


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

# Example 3:
head = [1, 2, 3, 2, 1]
ans = True
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if isPalindrome(root) == ans else "Fail")
