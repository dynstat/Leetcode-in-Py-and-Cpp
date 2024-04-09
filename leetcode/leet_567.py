# 567. Permutation in String
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English lette


from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    # s1 = "ab", s2 = "eidbaooo"
    lp = 0
    window_size = len(s1)

    # Initialize the right pointer (rp) to the end of the initial window
    # The window size is the length of s1, so rp is set to lp + window_size - 1, as the indexing starts from 0
    rp = lp + window_size - 1

    hmap1 = defaultdict(lambda: 0)
    hmap2 = defaultdict(lambda: 0)

    for ch in s1:
        hmap1[ch] += 1
    # hmap1 modified

    # Ensure the window size is exactly the length of s1 and within bounds of s2
    while (rp - lp) == window_size - 1 and rp < len(s2):
        hmap2 = defaultdict(lambda: 0)
        # looping on the new window
        for ch in s2[lp : rp + 1]:
            hmap2[ch] += 1
        if hmap2 == hmap1:
            return True
        else:
            lp += 1
            rp += 1

    return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))
    s1 = "a"
    s2 = "ab"
    print(checkInclusion(s1, s2))
