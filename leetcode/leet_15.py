from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    for i, val in enumerate(nums):
        # Skip duplicates for first number (since the array is sorted, duplicates will be next to each other)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        target = -1 * nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                ans.append([nums[i], nums[l], nums[r]])
                # Skip duplicates for second number (left pointer)
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Skip duplicates for third number (right pointer)
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1

    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([3, -2, 1, 0]))  # Expected output: [[-2, 1, 1]]
