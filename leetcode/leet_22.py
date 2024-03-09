# 22. Generate Parentheses
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


from typing import List


def generateParenthesis(n: int) -> List[str]:
    lc = n
    rc = n
    ans = []
    s = ""

    def brack(lc, rc, string):
        if lc <= 0 and rc <= 0:
            ans.append(string)
            return
        if lc > 0:
            string += "("
            lc -= 1
            brack(lc, rc, string)
        if rc > 0:
            string += ")"
            rc -= 1
            brack(lc, rc, string)

    brack(lc, rc, s)
    return ans


if __name__ == "__main__":
    print(generateParenthesis(3))
