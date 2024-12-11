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

    def similarPairs2(self, words: List[str]) -> int:
        hashmap = {}
        count = 0
        for idx, word in enumerate(words):
            tup = tuple(set(word))
            if tup not in hashmap:
                hashmap[tup] = 1
            else:
                hashmap[tup] += 1
        for i, val in hashmap.items():
            if val > 1:
                count += val
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.similarPairs2(["aba", "aabb", "abcd", "bac", "aabc"]))
    print(s.similarPairs2(["aabb", "ab", "ba"]))

# NOTE: Simply using the hasmap to count the numbers of strings matching the unique tuple wont give the answer, i need to find the each combination of the pairs.
