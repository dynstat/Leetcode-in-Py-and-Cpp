# 875. Koko Eating Bananas
# Attempted
# Medium
# Topics
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    piles.sort()
    max_k = piles[-1]
    min_k = 1
    ans_k = 0
    while min_k <= max_k:
        total_hours = 0
        mid_k = min_k + (max_k - min_k) // 2
        for i in piles:
            hours = i / mid_k
            round_hours = -(-hours // 1)  # round towards +infinity (ceil)
            total_hours += round_hours
        if total_hours <= h:
            ans_k = mid_k
            max_k = mid_k - 1
        elif total_hours > h:
            min_k = mid_k + 1
    return ans_k


if __name__ == "__main__":
    piles_test = [
        [312884470],
        [312884470],
        [3, 6, 7, 11],
        [30, 11, 23, 4, 20],
        [30, 11, 23, 4, 20],
    ]
    h_test = [968709470, 312884469, 8, 5, 6]

    for piles, h in zip(piles_test, h_test):
        result = minEatingSpeed(piles, h)
        print(piles, h, "->", result)
