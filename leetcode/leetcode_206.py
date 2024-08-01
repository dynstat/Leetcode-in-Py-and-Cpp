# 206. Reverse Linked List
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.4M
# Submissions
# 5.6M
# Acceptance Rate
# 77.2%


from typing import Optional
from pydantic import BaseModel


# Definition for singly-linked list.
class ListNode(BaseModel):
    val: int
    next: Optional["ListNode"]


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1,2,3,4,5] -> head is of the type [ListNode,....]
        prev = None
        curr = head
        nex = None

        while curr:
            nex = curr.next  # nex => 2
            curr.next = prev  # None <- 1  2 -> 3 -> 4 -> 5
            prev = curr
            curr = nex
        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    out = Solution().reverseList(head)
    print(out.val)
    print(out.next.val)
    print(out.next.next.val)
    print(out.next.next.next.val)
    print(out.next.next.next.next.val)
