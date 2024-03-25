// # Code
// # Testcase
// # Testcase
// # Test Result
// # 153. Find Minimum in Rotated Sorted Array
// # Medium
// # Topics
// # Companies
// # Hint
// # Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// # [4,5,6,7,0,1,2] if it was rotated 4 times.
// # [0,1,2,4,5,6,7] if it was rotated 7 times.
// # Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// # Given the sorted rotated array nums of unique elements, return the minimum element of this array.

// # You must write an algorithm that runs in O(log n) time.

// # Example 1:

// # Input: nums = [3,4,5,1,2]
// # Output: 1
// # Explanation: The original array was [1,2,3,4,5] rotated 3 times.
// # Example 2:

// # Input: nums = [4,5,6,7,0,1,2]
// # Output: 0
// # Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
// # Example 3:

// # Input: nums = [11,13,15,17]
// # Output: 11
// # Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

// # Constraints:

// # n == nums.length
// # 1 <= n <= 5000
// # -5000 <= nums[i] <= 5000
// # All the integers of nums are unique.
// # nums is sorted and rotated between 1 and n times.
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
    int findMin(const vector<int> &nums)
    {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;
        int mid_val = 0;
        int ans = 5000;
        while (left <= right)
        {
            mid = left + (right - left) / 2;
            mid_val = nums[mid];
            int lv = nums[left];
            int rv = nums[right];
            if (mid_val < nums[left])
            {
                ans = min(ans, mid_val);
                right = mid - 1;
            }
            else if (mid_val >= nums[left])
            {
                ans = min(ans, nums[left]);
                left = mid + 1;
            }
            else
            {
                break;
            }
        }
        return ans;
    }
};

int main()
{
    Solution s;
    int ret = s.findMin(vector<int>{5, 1, 2, 3, 4});
    cout << ret << endl;
}