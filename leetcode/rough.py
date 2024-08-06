from typing import List, Optional


# def largestRectangleArea(heights: List[int]) -> int:
#     # heights = [2,1,5,6,2,3]
#     left = []
#     right = []
#     max_area = 0
#     size = len(heights)
#     # right boundary
#     for idx, val in enumerate(heights):
#         r_idx = idx + 1
#         while r_idx < size and val <= heights[r_idx]:
#             r_idx += 1
#         right.append(
#             r_idx
#         )  # it includes the width of the each bar (=1) that has to be subtracted later

#     # left boundary
#     for idx in range(len(heights) - 1, -1, -1):
#         l_idx = idx - 1
#         while l_idx >= 0 and heights[idx] <= heights[l_idx]:
#             l_idx -= 1
#         left.append(l_idx)
#     # reversing the right boundary as appending the items is left to right but the items/indices
#     # we are iterating through are right to left.
#     left = left[::-1]
#     for idx in range(size):
#         max_area = max(max_area, heights[idx] * (right[idx] - left[idx] - 1))
#     return max_area


# largestRectangleArea([2, 1, 5, 6, 200, 3])


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # __str__ is used for creating output for end user
        return f"{id(self)} ({self.val})"

    def __repr__(self):
        # __repr__ is used for creating output for developer (debugging)
        return f"{id(self)} ({self.val})"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        all_nodes = []
        temp = head
        while temp:
            all_nodes.append(temp)
            temp = temp.next

        #  all_nodes = [1,2,3,4,5]
        temp = head
        for i in range(1, len(all_nodes)):
            # i = 0
            j = len(all_nodes) - i
            if i > j:
                temp.next = None
                break
            if i == j:
                temp.next = all_nodes[i]
                temp = temp.next
                temp.next = None
                break
            temp.next = all_nodes[j]
            temp = temp.next
            temp.next = all_nodes[i]
            temp = temp.next

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    out = Solution().reorderList(head)
    print(out)
    print(out.next)
    print(out.next.next)
    print(out.next.next.next)
