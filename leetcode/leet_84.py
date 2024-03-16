# 84. Largest Rectangle in Histogram
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104


def largestRectangleArea(heights):
    stack = [-1]  # Initialize stack with a sentinel value
    max_area = 0  # To keep track of the maximum area found

    for i, h in enumerate(heights):
        # While the current bar is lower than the top of the stack
        while stack[-1] != -1 and heights[stack[-1]] > h:
            # Pop the stack and calculate the area of the rectangle
            # with the popped bar as the smallest bar
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        # Push the current index to the stack
        stack.append(i)

    # Clear the stack of remaining bars
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area
