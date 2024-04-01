// # 3. Longest Substring Without Repeating Characters
// # Attempted
// # Medium
// # Topics
// # Companies
// # Given a string s, find the length of the longest
// # substring
// #  without repeating characters.

// # Example 1:

// # Input: s = "abcabcbb"
// # Output: 3
// # Explanation: The answer is "abc", with the length of 3.
// # Example 2:

// # Input: s = "bbbbb"
// # Output: 1
// # Explanation: The answer is "b", with the length of 1.
// # Example 3:

// # Input: s = "pwwkew"
// # Output: 3
// # Explanation: The answer is "wke", with the length of 3.
// # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// # Constraints:

// # 0 <= s.length <= 5 * 104
// # s consists of English letters, digits, symbols and spaces.

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
    int lengthOfLongestSubstring(string s)
    {
        int l = 0;
        int r = 0;
        unordered_map<string, int> hmap;
        string val;
        int max_count = 0;
        while (r < s.length())
        {
            val = s[r];
            if (hmap.find(val) == hmap.end()) // val not found in hmap as any key
            {
                hmap[val] += 1;
                r += 1;
            }
            else
            {
                val = s[l];
                hmap[val] -= 1;
                if (hmap[val] == 0)
                {
                    hmap.erase(val);
                }
                l += 1;
            }
            max_count = max(max_count, (r - l));
        }

        return max_count;
    }
};

int main()
{
    Solution sol;
    string s = "abcabcbb";
    cout << sol.lengthOfLongestSubstring(s) << endl;
    return 0;
}