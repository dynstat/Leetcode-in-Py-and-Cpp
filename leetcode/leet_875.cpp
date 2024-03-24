// # 875. Koko Eating Bananas
// # Attempted
// # Medium
// # Topics
// # Companies
// # Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

// # Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

// # Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

// # Return the minimum integer k such that she can eat all the bananas within h hours.

// # Example 1:

// # Input: piles = [3,6,7,11], h = 8
// # Output: 4
// # Example 2:

// # Input: piles = [30,11,23,4,20], h = 5
// # Output: 30
// # Example 3:

// # Input: piles = [30,11,23,4,20], h = 6
// # Output: 23

// # Constraints:

// # 1 <= piles.length <= 104
// # piles.length <= h <= 109
// # 1 <= piles[i] <= 109

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        // # Input: piles = [30,11,23,4,20], h = 5
        // # Output: 30
        sort(piles.begin(), piles.end());
        long min_k = 1;
        long max_k = piles[piles.size() - 1];
        long ans_k;
        while (min_k <= max_k)
        {
            long mid_k = min_k + (long)(max_k - min_k) / 2;
            long hours = 0;
            for (auto &p : piles)
            {
                hours += (p + mid_k - 1) / mid_k; // This ensures upper limit rounding
            }
            if (hours > h)
            {
                min_k = mid_k + 1;
            }
            else if (hours <= h)
            {
                ans_k = mid_k;
                max_k = mid_k - 1;
            }
        }
        return (int)ans_k;
    }
};

int main()
{
    Solution sol;
    vector<int> piles = {805306368, 805306368, 805306368};
    int h = 1000000000;
    cout << sol.minEatingSpeed(piles, h) << endl;
    piles = {3, 6, 7, 11};
    h = 8;
    cout << sol.minEatingSpeed(piles, h) << endl;
    piles = {30, 11, 23, 4, 20};
    h = 5;
    cout << sol.minEatingSpeed(piles, h) << endl;
    piles = {30, 11, 23, 4, 20};
    h = 6;
    cout << sol.minEatingSpeed(piles, h) << endl;
    return 0;
}
