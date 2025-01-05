# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


# ``````````````````````````````````````````````````@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from typing import *


def maxArea(height: List[int]) -> int:
    # two pointers approach
    l = 0
    r = len(height) - 1
    ans = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        ans = max(ans, area)

        # conditon to move pointers - since out of the current lines, we will keep the one with
        # the more height and move the pointer for the shorter height line to the next one since,
        # we need to find the max area, and it makes sense to lose the shorter line instead of
        # the larger one.
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return ans


if __name__ == "__main__":
    test_list = [1, 1]
    test_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(test_list))
