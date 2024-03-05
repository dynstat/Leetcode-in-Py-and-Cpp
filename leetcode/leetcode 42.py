# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


from typing import List


def trap(height: List[int]) -> int:
    # Initialize the length of the height array
    arr_len = len(height)
    # Set the initial left and right pointers
    left = 0
    right = arr_len - 1

    # Initialize the maximum height from the left and right
    max_left = height[left]
    max_right = height[right]

    # Initialize the variable to store the total trapped water area
    area = 0

    # Loop until the left pointer is less than the right pointer
    while left < right:
        # If the max height on the left is less than on the right
        if max_left < max_right:
            # If the next left height is greater than the current max left height
            if height[left + 1] > max_left:
                # Update the max left height
                max_left = height[left + 1]
                # Move the left pointer to the right
                left += 1
            else:
                # Otherwise, Calculate the trapped water at the current position and add to the total area.
                # Since the max left height is less than the max right height, the trapped water at the current position is the difference between the max left height and the current height
                area += max_left - height[left + 1]
                # Move the left pointer to the right
                left += 1

        # Similar case but for the right side, since the max right height is less than the max left height
        else:
            # If the next right height is greater than the current max right height
            if height[right - 1] > max_right:
                # Update the max right height
                max_right = height[right - 1]
                # Move the right pointer to the left
                right -= 1
            else:
                # Calculate the trapped water at the current position and add to the total area
                area += max_right - height[right - 1]
                # Move the right pointer to the left
                right -= 1
    # Return the total trapped water area
    return area


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
