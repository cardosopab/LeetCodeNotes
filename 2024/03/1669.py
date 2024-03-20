# 1669. Merge In Between Linked Lists
# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.

import sys

sys.path.append("../..")
from ListNode import ListNode


def mergeInBetween(list1, a, b, list2):
    curr = list1

    # Iterate to before a
    # While i < a - 1
    i = 0
    while i < a - 1:
        curr = curr.next
        i += 1

    # Create start for list2
    start = curr

    # Iterate to b which becomes entry point for end of list2
    # While i <= b
    while i <= b:
        curr = curr.next
        i += 1

    # Set start.next to list2
    start.next = list2

    # Iterate list2 to get last node
    # While list2.next
    while list2.next:
        list2 = list2.next

    # Set list2.next to curr
    list2.next = curr

    # Return list1
    list1 = ListNode().linkedListToArray(list1)
    return list1


# Example 1:
list1 = [10, 1, 13, 6, 9, 5]
a = 3
b = 4
list2 = [1000000, 1000001, 1000002]
ans = [10, 1, 13, 1000000, 1000001, 1000002, 5]
root1 = ListNode().arrayToLinkedList(list1, len(list1))
root2 = ListNode().arrayToLinkedList(list2, len(list2))
print("Pass" if mergeInBetween(root1, a, b, root2) == ans else "Fail")
# Example 2:
list1 = [0, 1, 2, 3, 4, 5, 6]
a = 2
b = 5
list2 = [1000000, 1000001, 1000002, 1000003, 1000004]
ans = [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
root1 = ListNode().arrayToLinkedList(list1, len(list1))
root2 = ListNode().arrayToLinkedList(list2, len(list2))
print("Pass" if mergeInBetween(root1, a, b, root2) == ans else "Fail")
