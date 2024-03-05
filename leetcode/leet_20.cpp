// 20. Valid Parentheses
// Easy
// Topics
// Companies
// Hint
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false

// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.

#include <string>
#include <vector>
#include <unordered_map>
#include <stack>
#include <iostream>
#include <set>

using namespace std;

bool isValid(string s)
{
    // d = { ')' : '(', '}' : '{', ']' : '[' }

    // s1 = {'(','{','['}
    // s2 = {')','}',']'}

    set<char> s1({'(', '{', '['});
    set<char> s2({')', '}', ']'});
    unordered_map<char, char> d({{')', '('}, {'}', '{'}, {']', '['}});
    stack<char> b_stack;
    for (auto bracket : s)
    {
        if (s1.find(bracket) != s1.end())
        {
            b_stack.push(bracket);
        }
        else if (s2.find(bracket) != s2.end())
        {
            if (b_stack.empty())
            {
                return false;
            }
            char close_bracket = b_stack.top();
            b_stack.pop();
            if (d[bracket] != close_bracket)
            {
                return false;
            }
        }
    }
    if (b_stack.empty())
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    cout << isValid("()") << endl;
    cout << isValid("()[]{}") << endl;
    cout << isValid("(]") << endl;
    cout << isValid("([)]") << endl;
    cout << isValid("{[]}") << endl;
}
