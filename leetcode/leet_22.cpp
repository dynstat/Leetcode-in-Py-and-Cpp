// # 22. Generate Parentheses
// # Medium
// # Topics
// # Companies
// # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

// # Example 1:

// # Input: n = 3
// # Output: ["((()))","(()())","(())()","()(())","()()()"]
// # Example 2:

// # Input: n = 1
// # Output: ["()"]

// # Constraints:

// # 1 <= n <= 8
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
private:
    vector<string> ans;
    void brack(string str, int l, int r, int n)
    {

        if (l == n && r == n)
        {
            ans.push_back(str);
            return;
        }

        if (l < n)
        {
            brack(str + '(', l + 1, r, n);
        }
        if (r < l)
        {
            brack(str + ')', l, r + 1, n);
        }
    }

public:
    vector<string> generateParenthesis(int n)
    {
        int l = 0;
        int r = 0;
        brack("", l, r, n);
        return ans;
    }
};

int main()
{
    Solution S;
    vector<string> v;
    v = S.generateParenthesis(3);
    for (const auto &str : v)
    {
        cout << str << endl; // Print each string on a new line
    }
}