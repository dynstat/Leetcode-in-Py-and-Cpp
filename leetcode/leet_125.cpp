#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

bool isPalindrome(string s)
{

    vector<string> temp;
    char *left = &s[0];
    char *right = &s[s.length() - 1];
    // for (int i = 0; i < (int)((s.length()) / 2); i++)
    while (left < right)
    {
        if (!isalnum(*left))
        {
            left++;
            continue;
        }
        if (!isalnum(*right))
        {
            right--;
            continue;
        }

        if (tolower(*left) != tolower(*right))
        {
            return false;
        }
        left++;
        right--;
        /*cout << "left->" << *left << " "
             << "right->" << *right; */
    }
    return true;
}
int main()
{
    string s = "A man, a plan, a canal: Panama";
    // s = "race a car";
    s = "a.b,.";
    cout << isPalindrome(s) << endl;
    return 0;
}
