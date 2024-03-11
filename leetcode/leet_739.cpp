// # 739. Daily Temperatures
// # Attempted
// # Medium
// # Topics
// # Companies
// # Hint
// # Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// # Example 1:

// # Input: temperatures = [73,74,75,71,69,72,76,73]
// # Output: [1,1,4,2,1,1,0,0]
// # Example 2:

// # Input: temperatures = [30,40,50,60]
// # Output: [1,1,1,0]
// # Example 3:

// # Input: temperatures = [30,60,90]
// # Output: [1,1,0]

// # Constraints:

// # 1 <= temperatures.length <= 105
// # 30 <= temperatures[i] <= 100

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <stack>

using namespace std;

class Solution
{
public:
    // my solution
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        stack<int> st;
        int len = temperatures.size();
        vector<int> ans(len, 0);
        for (int i = len - 1; i >= 0; i--)
        {
            int curr_val = temperatures[i];
            if (st.empty())
            {
                st.push(i); // pushing the index of the current number
                ans[i] = 0;
                continue;
            }
            while (!st.empty())
            {
                int top_index = st.top();
                int top_val = temperatures[top_index];
                if (curr_val >= top_val)
                {
                    st.pop();
                    continue;
                }
                else if (curr_val < top_val)
                {
                    int index_diff = top_index - i;
                    ans[i] = index_diff;
                    st.push(i);
                    break;
                }
            }
            if (st.empty())
            {
                ans[i] = 0;
                st.push(i);
            }
        }
        return ans;
    }
    // more consise method
    vector<int> dailyT(vector<int> &temperatures)
    {
        int len = temperatures.size();
        vector<int> ans(len, 0); // Initialize with size `len` and fill with 0s
        stack<int> st;           // Will store indices of temperatures

        for (int i = 0; i < len; i++)
        {
            while (!st.empty() && temperatures[i] > temperatures[st.top()])
            {
                int index = st.top();
                st.pop();
                ans[index] = i - index; // Calculate the difference
            }
            st.push(i); // Push current index onto the stack
        }
        return ans;
    }
};

int main()
{
    Solution s;
    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
    vector<int> ans = s.dailyTemperatures(temperatures);
    vector<int> ans = s.dailyT(temperatures);
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}
