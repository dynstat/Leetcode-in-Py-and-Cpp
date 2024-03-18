# Code
# Note
# Note
# Testcase
# Testcase
# Test Result
# 704. Binary Search
# Solved
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        mid_val = nums[mid]
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
