
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int maxArea(vector<int> &height)
{
    // height = [1,8,6,2,5,4,8,3,7]
    int l = 0;
    int r = (int)height.size() - 1;
    int max_product = 0;
    while (l < r)
    {
        int w = r - l;
        int h = min(height[l], height[r]);
        int curr_product = w * h;
        max_product = max(max_product, curr_product);

        // Now moving the pointers
        if (height[l] < height[r])
        {
            l++;
        }
        else
        {
            r--;
        }
    }
    return max_product;
}
int main()
{
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << maxArea(height) << endl;
}
