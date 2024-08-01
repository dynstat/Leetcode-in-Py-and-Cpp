# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # list1 = [1,2,4], list2 = [1,3,4]  -> each item is a node
        merged_head = ListNode()
        merged_dummy = merged_head
        print(id(list1), id(list2))
        while (
            list1 and list2
        ):  # when any of the list1 or list2 is not None, then go inside
            if list1.val <= list2.val:
                merged_dummy.next = list1
                list1 = list1.next
            else:
                merged_dummy.next = list2
                list2 = list2.next
            merged_dummy = merged_dummy.next

        if list1:
            merged_dummy.next = list1
        else:
            merged_dummy.next = list2
        print(id(merged_head.next))
        return merged_head.next


if __name__ == "__main__":
    sol = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    print(sol.mergeTwoLists(list1, list2))
