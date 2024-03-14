#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        // target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        vector<pair<int, double>> pt_pair;
        int len = position.size();
        for (int i = 0; i < len; i++)
        {
            double time = position[i] / speed[i];
            pt_pair.push_back({position[i], time});
        }

        // sort the pt_pair according to the positons
        sort(pt_pair.begin(), pt_pair.end(),
             [](const pair<int, double> &a, const pair<int, double> &b)
             { return a.first > b.first; });
        // reverse(pt_pair.begin(), pt_pair.end());

        int fleets = 0;
        double lastTime = 0;
        for (auto &pt : pt_pair)
        {

            int p = pt.first;
            double t = pt.second;

            if (lastTime == 0)
            {
                lastTime = t;
                fleets += 1;
                continue;
            }
            if (t <= lastTime)
            {
                continue;
            }
            else if (t > lastTime)
            {
                fleets += 1;
                lastTime = t;
            }
        }
        return fleets;
    }
};

int main()
{
    Solution sol;
    vector<int> position = {10, 8, 0, 5, 3};
    vector<int> speed = {2, 4, 1, 1, 3};
    int target = 12;
    cout << sol.carFleet(target, position, speed) << endl;
}
