# Code
# Testcase
# Testcase
# Test Result
# 153. Find Minimum in Rotated Sorted Array
# Medium
# Topics
# Companies
# Hint
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


from typing import List


def findMin(nums: List[int]) -> int:
    # nums = [5, 1, 2, 3, 4]
    # output -> 1   i.e. the minimum number in the array.

    left = 0
    right = len(nums) - 1
    min_val = nums[0]  # just some arbitrary value for the start
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = nums[mid]

        if mid_val >= nums[left]:
            min_val = min(nums[left], min_val)
            left = mid + 1
        elif mid_val < nums[left]:
            min_val = min(mid_val, min_val)
            right = mid - 1
    return min_val


if __name__ == "__main__":
    nums_test = [5, 1, 2, 3, 4]
    nums_test = [2, 1]
    print(findMin(nums_test))
