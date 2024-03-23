# 143. Reorder List
# Medium
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
import sys

sys.path.append("../..")

from ListNode import ListNode


def reorderList(head):
    slow, fast, prev = head, head, None

    # Find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Iterate adding alternating nodes
    first_half, second_half = head, prev
    while second_half.next:
        # Save pointers
        first_half_next = first_half.next
        second_half_next = second_half.next

        # Intertwine pointers
        first_half.next = second_half
        second_half.next = first_half_next

        # Move forward
        first_half = first_half_next
        second_half = second_half_next

    ans = ListNode().linkedListToArray(head)
    print(ans)
    return ans


# Example 1:
head = [1, 2, 3, 4]
ans = [1, 4, 2, 3]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reorderList(root) == ans else "Fail")
# Example 2:
head = [1, 2, 3, 4, 5]
ans = [1, 5, 2, 4, 3]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reorderList(root) == ans else "Fail")


# NOTE: Solution doesn't work on LeetCode
def reorderList(head):
    slow, fast, prev = head, head, None

    # Find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Iterate adding alternating nodes
    slow = head
    new_head = ListNode()
    idx = 0
    while slow and prev:
        if idx % 2 == 0:
            ptr = new_head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(slow.val)
            slow = slow.next
        else:
            ptr = new_head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(prev.val)
            prev = prev.next
        idx += 1

    head = new_head.next
    ans = ListNode().linkedListToArray(head)
    print(ans)
    return ans


# Example 1:
head = [1, 2, 3, 4]
ans = [1, 4, 2, 3]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reorderList(root) == ans else "Fail")
# Example 2:
head = [1, 2, 3, 4, 5]
ans = [1, 5, 2, 4, 3]
root = ListNode().arrayToLinkedList(head, len(head))
print("Pass" if reorderList(root) == ans else "Fail")
