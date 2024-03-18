
// Code
// Note
// Note
// Testcase
// Testcase
// Test Result
// 704. Binary Search
// Solved
// Easy
// Topics
// Companies
// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4
// Example 2:

// Input: nums = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in nums so return -1

// Constraints:

// 1 <= nums.length <= 104
// -104 < nums[i], target < 104
// All the integers in nums are unique.
// nums is sorted in ascending order.

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
        int len = nums.size();
        int left = 0;
        int right = len - 1;
        int mid = 0;
        int mid_val = 0;
        while (left <= right)
        {
            mid = left + (int)((right - left) / 2);
            mid_val = nums[mid];
            if (mid_val == target)
            {
                return mid;
            }
            else if (mid_val > target)
            {
                right = mid - 1;
            }
            else if (mid_val < target)
            {
                left = mid + 1;
            }
        }
        return -1;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;
    cout << sol.search(nums, target) << endl;
}
