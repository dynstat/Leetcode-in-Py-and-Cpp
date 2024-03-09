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
    lc = 0
    rc = 0
    ans = []
    s = ""
    count = 0

    def brack(lc, rc, string, count, type):
        nonlocal n
        print("\ncount: ", count, end=" |  ")
        print("type : ", type, end="  |  ")
        print("string : ", string, end=f"{(10 - len(string))* " "}|  ")
        print("lc : ", lc, end="  |  ")
        print("rc : ", rc, end="  |  ")

        if lc == n and rc == n:
            ans.append(string)
            print(f"APPENDED - {string}")
            return
        if lc <= n and rc <= n:
            # string += "("
            # lc += 1
            brack(lc + 1, rc, string + "(", count + 1, "left ")

        if rc < lc:
            # string += ")"
            # rc += 1
            brack(lc, rc + 1, string + ")", count + 1, "right")

    brack(lc, rc, s, 0, "START")
    return ans


if __name__ == "__main__":
    print(generateParenthesis(3))
