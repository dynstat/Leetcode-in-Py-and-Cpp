# LeetCode Problem 143: Reorder List
#
# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
# Example 1:
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Example 2:
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000


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

# creating linked list
head = n1
n1.next = n2
n2.next = n3
n3.next = n4

node_list = [n1, n2, n3, n4]


head = node_list[0]
temp = head
for i in range(1, len(node_list)):
    j = len(node_list) - i
    if i == j:
        temp.next = node_list[i]
        temp = temp.next
        temp.next = None
    if i >= j:
        temp.next = None
        break

    temp.next = node_list[j]
    temp = temp.next
    temp.next = node_list[i]
    temp = temp.next


if __name__ == "__main__":
    print(head)
    print(head.next)
    print(head.next.next)
    print(head.next.next.next)
