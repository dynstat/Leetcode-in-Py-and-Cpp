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

    hmap = defaultdict(lambda: 0)
    # hmap[s[left]] += 1

    def isValid(left, right, k=k):
        if ((right - left + 1) - max(hmap.values())) <= k:
            return True
        else:
            return False

    while right <= len(s) - 1 and left <= len(s) - 1:
        hmap[s[right]] += 1
        if isValid(left, right):
            max_len = max(max_len, (right - left + 1))
        else:
            while not isValid(left, right):
                hmap[s[left]] -= 1
                left += 1
            max_len = max(max_len, (right - left + 1))
        right += 1
    return max_len


if __name__ == "__main__":
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    print(characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))
    s = "AABA"
    k = 0
    print(characterReplacement(s, k))
    s = "AAAA"
    k = 2
    print(characterReplacement(s, k))
