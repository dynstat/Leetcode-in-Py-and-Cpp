from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    # heights = [2,1,5,6,2,3]
    left = []
    right = []
    max_area = 0
    size = len(heights)
    # right boundary
    for idx, val in enumerate(heights):
        r_idx = idx + 1
        while r_idx < size and val <= heights[r_idx]:
            r_idx += 1
        right.append(
            r_idx
        )  # it includes the width of the each bar (=1) that has to be subtracted later

    # left boundary
    for idx in range(len(heights) - 1, -1, -1):
        l_idx = idx - 1
        while l_idx >= 0 and heights[idx] <= heights[l_idx]:
            l_idx -= 1
        left.append(l_idx)
    # reversing the right boundary as appending the items is left to right but the items/indices
    # we are iterating through are right to left.
    left = left[::-1]
    for idx in range(size):
        max_area = max(max_area, heights[idx] * (right[idx] - left[idx] - 1))
    return max_area


largestRectangleArea([2, 1, 5, 6, 200, 3])
