# 150. Evaluate Reverse Polish Notation
# Medium
# Topics
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
from typing import List


def evalRPN(self, tokens: List[str]) -> int:
    temp = []
    s = {"+", "-", "*", "/"}
    first = 0
    second = 0
    for ch in tokens:
        if ch in s and len(temp) >= 2:
            second = int(temp.pop())
            first = int(temp.pop())
            if ch == "+":
                new = first + second
            elif ch == "-":
                new = first - second
            elif ch == "*":
                new = first * second
            elif ch == "/":
                # this will find the absolute value of the decimal number...
                # by removing the decimal part. This will make it look like it is
                # rounding off towards zero (not negative infinity)
                new = int(first / second)
            temp.append(new)
        else:
            temp.append(int(ch))
    return temp[0]


if __name__ == "__main__":
    print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(
        evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    )
