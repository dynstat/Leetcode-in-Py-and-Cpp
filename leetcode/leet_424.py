# 424. Longest Repeating Character Replacement
# Medium
# Topics
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
from typing import List
from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    left = 0
    right = 0
    max_len = 0
    window_len = 1
    hmap = defaultdict(lambda: 0)
    flag = 0
    while right <= len(s) - 1 and left <= len(s) - 1:
        l_val = s[left]
        r_val = s[right]

        if not flag:
            hmap[r_val] += 1

        if right == len(s) - 1:
            flag = 1
        else:
            pass
        if l_val == r_val:
            if (window_len - max(hmap.values())) <= k:
                max_len = max(window_len, max_len)
                if right < len(s) - 1:
                    right += 1
                    window_len += 1
                else:
                    left += 1
                    window_len -= 1
                    hmap[l_val] -= 1
            else:
                left += 1
                window_len -= 1
                hmap[l_val] -= 1

        else:  # left and the right values are not equal.
            if (window_len - max(hmap.values())) <= k:
                # hmap[r_val] += 1
                max_len = max(window_len, max_len)
                right += 1
                window_len += 1

            else:
                left += 1
                right += 1
                hmap[l_val] -= 1
                # window_len -= 1
    return max_len


if __name__ == "__main__":
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    print(characterReplacement(s, k))
    s = "AAAA"
    k = 2
    print(characterReplacement(s, k))
    s = "AABA"
    k = 0
    print(characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))
