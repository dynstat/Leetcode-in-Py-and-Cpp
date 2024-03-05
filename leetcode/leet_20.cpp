
#include <string>
#include <vector>
#include <unordered_map>
#include <stack>
#include <iostream>
#include <set>
#include <unordered_map>

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
