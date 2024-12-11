from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0

        for i in range(len(words)):
            # inner loop will iterate till the (i-1) index and compare the elements to the left of it
            # This restricts the double or multiple comparisons.
            for j in range(i):
                if set(words[i]) == set(words[j]):
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))

# NOTE: Using the hashmap will be the better method.
# keys can be the tuple of unique pairs and iterating through one loop can determine the counts
# of existing tuple (of unique chars) or add new ones if not exist in the dictionary/hashmap
