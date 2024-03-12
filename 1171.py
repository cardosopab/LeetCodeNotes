# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.

# Input: linked list
# Output: linked list without zero sum consecutives
# Solution: using a stack to hold the values, a prefix sum, and a set, if value
# seen before, pop the values until the matching value in seen
from ListNode import ListNode


def removeZeroSumSublists(head):
    dummy = head
    stack = []
    seen = set([0])
    prefix = 0

    while dummy:
        prefix += dummy.val
        stack.append(dummy.val)
        if prefix in seen:
            curr_prefix = prefix
            prefix -= stack[-1]
            stack.pop()
            while curr_prefix != prefix:
                seen.remove(prefix)
                prefix -= stack[-1]
                stack.pop()
        else:
            seen.add(prefix)
        dummy = dummy.next

    # NOTE: stack needs to be turned back to a linked list for LeetCode
    return stack


# Example 1:
head = [1, 2, -3, 3, 1]
ans = [3, 1]
root = ListNode().arrayToLinkedList(head, len(head))
# Note: The answer [1, 2, 1] would also be accepted.
print("Pass" if removeZeroSumSublists(root) == ans else "Fail")
# Example 2:
head = [1, 2, 3, -3, 4]
ans = [1, 2, 4]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if removeZeroSumSublists(root) == ans else "Fail")
# Example 3:
head = [1, 2, 3, -3, -2]
ans = [1]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if removeZeroSumSublists(root) == ans else "Fail")
# Example 4:
head = [0, 0]
ans = []
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if removeZeroSumSublists(root) == ans else "Fail")
