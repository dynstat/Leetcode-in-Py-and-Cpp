# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [1,2,4]
        if len(prices) < 2:
            return 0

        b = prices[0]  # 1
        s = prices[1]  # 2

        profit = 0
        i = 1
        while i <= len(prices) - 1:
            if s <= b:  # 1st loop ->  2 <= 1 ?? NO
                b = s
                if i < len(prices) - 1:
                    s = prices[i + 1]  # s = next index value (prices[i+1])
            else:
                profit = max(profit, (s - b))
                if i < len(prices) - 1:
                    s = prices[i + 1]  # s= 4
            i += 1
        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
