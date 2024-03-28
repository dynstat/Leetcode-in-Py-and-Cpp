// # 33. Search in Rotated Sorted Array
// # Medium
// # Topics
// # Companies
// # There is an integer array nums sorted in ascending order (with distinct values).

// # Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// # Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

// # You must write an algorithm with O(log n) runtime complexity.

// # Example 1:

// # Input: nums = [4,5,6,7,0,1,2], target = 0
// # Output: 4
// # Example 2:

// # Input: nums = [4,5,6,7,0,1,2], target = 3
// # Output: -1
// # Example 3:

// # Input: nums = [1], target = 0
// # Output: -1

// # Constraints:

// # 1 <= nums.length <= 5000
// # -104 <= nums[i] <= 104
// # All values of nums are unique.
// # nums is an ascending array that is possibly rotated.
// # -104 <= target <= 104

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>

using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        // int flag = 0;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int mid_value = nums[mid];

            if (target == mid_value)
            {
                // flag = 1;
                return mid;
            }

            /// Left side is sorted
            if (nums[left] <= mid_value)
            {
                if (target >= nums[left] && target < mid_value)
                {
                    right = mid - 1;
                }
                else
                {

                    left = mid + 1;
                }
            }
            /// right side is sorted
            else
            {
                if (target > mid_value && target <= nums[right])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    // vector<int> nums = {1, 3};
    // vector<int> nums = {3, 1};
    // vector<int> nums = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    std::cout << s.search(nums, 0) << std::endl;
}
