class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Function to insert node
    def insert(self, root, item):
        temp = ListNode(item)

        if root is None:
            root = temp
        else:
            ptr = root
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = temp

        return root

    # Function to convert array to linked list
    def arrayToLinkedList(self, arr, n):
        root = None
        for i in range(0, n, 1):
            root = ListNode().insert(root, arr[i])

        return root

    # Function to convert linked list to array
    def linkedListToArray(self, root):
        if not root:
            return
        nodeList = []
        dummy = root
        while dummy:
            nodeList.append(dummy.val)
            dummy = dummy.next

        return nodeList
