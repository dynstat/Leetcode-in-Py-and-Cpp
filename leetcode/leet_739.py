# 739. Daily Temperatures
# Attempted
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # temperatures = [73,74,75,71,69,72,76,73]
    t = temperatures
    ans = []
    stack = []

    for idx in range(len(t) - 1, -1, -1):
        popped = t[idx]
        if not stack:
            stack.append(idx)  # 73 pushed in first iteration
            ans.insert(0, 0)
            continue
        while stack:
            stack_top = t[stack[-1]]
            if popped >= stack_top:
                stack.pop()
                continue
            elif popped < stack_top:
                ans.insert(
                    0, stack[-1] - idx
                )  # stack value index - current index (tempreratures)
                stack.append(idx)
                break  # index of the "popped" item is added to the stack
        if len(stack) == 0:
            ans.insert(0, 0)
            stack.append(
                idx
            )  # pushing the index of that number to the "stack" which does not have any greater number in the "stack"
    return ans


if __name__ == "__main__":
    # print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
