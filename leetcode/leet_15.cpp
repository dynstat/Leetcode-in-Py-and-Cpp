#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<vector<int>> threeSum(vector<int> &nums)
{
    int len = nums.size();
    sort(nums.begin(), nums.end());
    // nums vector is sorted
    vector<vector<int>> ans;
    for (int i = 0; i < len; i++)
    {
        int fn = nums[i];
        int j = i + 1;
        int k = len - 1;
        int target = 0 - fn;
        if (i > 0 && nums[i - 1] == nums[i])
        {
            continue;
        }
        while (j < k)
        {

            int sn = nums[j];
            int tn = nums[k];
            if (sn + tn > target)
            {
                k--;
            }
            else if (sn + tn < target)
            {
                j++;
            }
            else
            {
                ans.push_back({fn, sn, tn});

                // after getting the correct numbers, we should check
                // the next numbers to avoid the duplicates.
                // (since the arrayy is sorted, the similar numbers would be close to each other)

                while (j < k && (nums[j] == nums[j + 1]))
                {
                    j += 1;
                }
                while (j < k && (nums[k] == nums[k - 1]))
                {
                    k -= 1;
                }
                j++; // moving to the next (left to right index)
                k--; // moving to the next (right to left index)
            }
        }
    }
    return ans;
}

int main()
{
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    // vector<int> nums = {0, 0, 0};
    vector<vector<int>> ans = threeSum(nums);
    for (auto i : ans)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << endl;
    }
}
