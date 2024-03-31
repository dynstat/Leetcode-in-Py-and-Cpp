# 3. Longest Substring Without Repeating Characters
# Attempted
# Medium
# Topics
# Companies
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(lambda: 0)
        l = 0
        r = 0
        c = 0
        max_c = 0
        sl_win = ""
        while r < len(s):
            sl_win = s[l : r + 1]
            val = s[r]
            if val not in hmap:
                hmap[val] += 1
                r += 1
            # value is already in the hmap
            else:
                val = s[l]
                hmap[val] -= 1
                if hmap[val] == 0:
                    hmap.pop(val)
                l += 1
            max_c = max(max_c, (r - l))
        return max_c


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("aab"))
    print(sol.lengthOfLongestSubstring("abcabcbb"))
