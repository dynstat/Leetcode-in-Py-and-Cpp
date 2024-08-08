from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)


head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


def traverse(temp):
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count


def removeNthFromEnd(head, n: int):
    # Create a temporary pointer to traverse the list
    temp = head
    # Get the total count of nodes in the list
    count = traverse(temp)

    # Initialize current and previous pointers to the head of the list
    curr = head
    prev = head

    # If the list is empty, return the head (which is None)
    if not head:
        return head

    # Traverse the list until the count becomes zero
    while count > 0:
        # If the current count is equal to n, we found the nth node from the end
        if count == n:
            # If the node to be removed is the only node in the list
            if prev.next is None:
                head = None
                return head
            else:
                # Remove the nth node from the end by updating the next pointer of the previous node
                prev.next = prev.next.next
                return head
        # Move the previous and current pointers one step forward
        prev = curr
        curr = curr.next
        # Decrement the count
        count -= 1


removeNthFromEnd(head, 1)


def BetterRemoveNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    sp = dummy
    fp = dummy
    for _ in range(n):
        fp = fp.next

    while fp.next:
        sp = sp.next
        fp = fp.next

    sp.next = sp.next.next
    return dummy.next


# NOTE: BetterRemoveNthFromEnd is a better solution than removeNthFromEnd because it does it in a single pass and uses a dummy node to simplify the code and avoid edge cases and it has a time complexity of O(n) and a space complexity of O(1) whereas removeNthFromEnd has a time complexity of O(n) and a space complexity of O(n) because it traverse the list again to remove the nth node from the end.


if __name__ == "__main__":
    # Link the nodes to form the list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9
    n9.next = n10

    # Test case 1: Remove the 2nd node from the end (which is node with value 4)
    head = BetterRemoveNthFromEnd(n1, 2)
    temp = head
    while temp:
        print(temp.val, end=" -> " if temp.next else "\n")
        temp = temp.next

    # Test case 2: Remove the 1st node from the end (which is node with value 5)
    head = BetterRemoveNthFromEnd(n1, 1)
    temp = head
    while temp:
        print(temp.val, end=" -> " if temp.next else "\n")
        temp = temp.next

    # Test case 3: Remove the 5th node from the end (which is node with value 1)
    head = BetterRemoveNthFromEnd(n1, 5)
    temp = head
    while temp:
        print(temp.val, end=" -> " if temp.next else "\n")
        temp = temp.next
