// # 84. Largest Rectangle in Histogram
// # Hard
// # Topics
// # Companies
// # Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

// # Example 1:

// # Input: heights = [2,1,5,6,2,3]
// # Output: 10
// # Explanation: The above is a histogram where width of each bar is 1.
// # The largest rectangle is shown in the red area, which has an area = 10 units.
// # Example 2:

// # Input: heights = [2,4]
// # Output: 4

// # Constraints:

// # 1 <= heights.length <= 105
// # 0 <= heights[i] <= 104

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution
{
public:
    int largestRectangleArea(vector<int> &heights)
    {
        // Initialize stack with a sentinel value to handle empty stack cases easily
        stack<int> s;
        s.push(-1);
        int max_area = 0; // Initialize max_area to 0. This will hold the maximum area of rectangle found.

        // Iterate through each bar in the histogram
        for (int i = 0; i < heights.size(); ++i)
        {
            // Check if the current bar is lower than the bar at the top of the stack
            // This means we've found a right boundary for the rectangle with height of the bar at the stack's top
            while (s.top() != -1 && heights[s.top()] > heights[i])
            {
                // Pop the top of the stack, as we will calculate the area of rectangle with this height
                int height = heights[s.top()]; // Height of the rectangle
                s.pop();
                // Calculate width of the rectangle.
                // Width is current index - index of the previous bar in stack - 1 (for the popped bar itself)
                int width = i - s.top() - 1;
                // Update max_area if the area of the current rectangle is greater
                max_area = max(max_area, height * width);
            }
            // Push the current index to the stack. This bar could be the start of a new potential rectangle
            s.push(i);
        }

        // After iterating through all bars, clear the stack of remaining bars
        // These bars did not find a right boundary that was lower than themselves
        while (s.top() != -1)
        {
            // Pop the top of the stack to calculate area of rectangle with this height
            int height = heights[s.top()];
            s.pop();
            // Calculate width for this rectangle. Since no smaller bar was found to the right,
            // the width extends till the end of the histogram
            int width = heights.size() - s.top() - 1;
            // Update max_area if the area of the current rectangle is greater
            max_area = max(max_area, height * width);
        }

        return max_area; // Return the maximum area found
    }
};

int main()
{
    Solution solution;
    vector<int> heights1 = {2, 1, 5, 6, 2, 3};
    cout << "Maximum area for heights [2,1,5,6,2,3]: " << solution.largestRectangleArea(heights1) << endl; // Expected output: 10

    vector<int> heights2 = {2, 4};
    cout << "Maximum area for heights [2,4]: " << solution.largestRectangleArea(heights2) << endl; // Expected output: 4

    return 0;
}
