// 74. Search a 2D Matrix
// Solved
// Medium
// Topics
// Companies
// You are given an m x n integer matrix matrix with the following two properties:

// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.

// You must write a solution in O(log(m * n)) time complexity.

// Example 1:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true
// Example 2:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 100
// -104 <= matrix[i][j], target <= 104

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
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        vector<int> m2;

        for (auto &subarr : matrix)
        {
            m2.insert(m2.end(), subarr.begin(), subarr.end());
        }

        // Simple Binary search as m2 is in ascending order
        int left = 0;
        int right = (int)m2.size() - 1;
        while (left <= right)
        {
            int mid = (int)(left + (right - left) / 2);
            int mid_val = m2[mid];

            if (mid_val == target)
            {
                return true;
            }
            else if (mid_val < target)
            {
                left = mid + 1;
            }
            else if (mid_val > target)
            {
                right = mid - 1;
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    int target = 3;
    cout << s.searchMatrix(matrix, target) << endl;
}
