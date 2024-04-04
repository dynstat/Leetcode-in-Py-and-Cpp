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


# def characterReplacement(s: str, k: int) -> int:
#     left = 0
#     right = 0
#     max_len = 0

#     hmap = defaultdict(lambda: 0)
#     # hmap[s[left]] += 1

#     def isValid(left, right, k=k):
#         if ((right - left + 1) - max(hmap.values())) <= k:
#             return True
#         else:
#             return False

#     while right <= len(s) - 1 and left <= len(s) - 1:
#         hmap[s[right]] += 1
#         if isValid(left, right):
#             max_len = max(max_len, (right - left + 1))
#         else:
#             while not isValid(left, right):
#                 hmap[s[left]] -= 1
#                 left += 1
#             max_len = max(max_len, (right - left + 1))
#         right += 1
#     return max_len


def characterReplacement(s: str, k: int) -> int:
    # Input: s = "AABABBA", k = 1
    if not s:
        return 0

    left = 0
    right = 0
    hmap = defaultdict(lambda: 0)
    hmap[s[0]] = 1
    max_len_result = 1

    while left <= right and right <= len(s) - 1:
        if (right - left + 1) - max(hmap.values()) <= k:
            max_len_result = max(max_len_result, right - left + 1)
            right += 1
            if right < len(s):
                hmap[s[right]] += 1
        else:
            hmap[s[left]] -= 1
            left += 1
            max_len_result = max(max_len_result, right - left + 1)
    return max_len_result


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    print(characterReplacement(s, k))
    s = "AABA"
    k = 0
    print(characterReplacement(s, k))
    s = "AAAA"
    k = 2
    print(characterReplacement(s, k))


# 1. Purpose: The function finds the length of the longest substring that can be formed by replacing at most k characters in the string s.
# 2. Sliding Window Technique: Uses a sliding window approach with two pointers, left and right, to explore possible substrings.
# 3. HashMap Usage: Utilizes a defaultdict to keep track of the count of each character within the current window (substring between left and right).
# 4. Window Expansion: The window expands by moving the right pointer to the right if the number of characters that need to be replaced to make the substring uniform does not exceed k.
# 5. Window Contraction: If the condition fails (more than k replacements needed), the window contracts from the left by moving the left pointer to the right and adjusting the character counts.
# 6. Max Length Calculation: Continuously updates the maximum length of the valid substring (max_len_result) during both expansion and contraction of the window.
