// O(N) time | O(N) space
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int trap(vector<int> &height)
{
    // height = [0,1,0,2,1,0,1,3,2,1,2,1]
    // time complexity = O(N)
    // space complexity = O(2N)

    int len = height.size();
    vector<int> maxleft(len);
    vector<int> maxright(len);
    int maxL = height[0];
    int maxR = height[len - 1];
    int area = 0;
    for (int i = 1; i < len; i++)
    {
        maxleft[i] = maxL;
        maxright[len - i - 1] = maxR;
        maxL = max(maxL, height[i]);
        maxR = max(maxR, height[len - i - 1]);
    }
    for (int j = 0; j < len; j++)
    {
        int a = min(maxleft[j], maxright[j]) - height[j];
        if (a > 0)
        {
            area += a;
        }
    }
    return area;
}

// O(N) time | O(1) space

int trap2(vector<int> &height)
{
    // using 2 pointers method
    int len = height.size();
    int left = 0;
    int right = len - 1;

    int max_left = height[left];
    int max_right = height[right];
    int area = 0;
    while (left < right)
    {
        if (max_left < max_right)
        {
            if (max_left < height[left + 1])
            {
                max_left = height[left + 1];
                left++;
            }
            else
            {
                area += min(max_left, max_right) - height[left + 1];
                left++;
            }
        }
        else
        {
            if (max_right < height[right - 1])
            {
                max_right = height[right - 1];
                right--;
            }
            else
            {
                area += min(max_left, max_right) - height[right - 1];
                right--;
            }
        }
    }
    return area;
}

int main()
{
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << trap2(height) << endl;
}
