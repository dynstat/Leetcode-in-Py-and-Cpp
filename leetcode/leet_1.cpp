#include <vector>
#include <unordered_map>
#include <iostream>
#include <typeinfo>

std::vector<int> twoSum(std::vector<int> &nums, int target)
{
    std::unordered_map<int, int> store;
    std::vector<int> temp;
    int len = nums.size();

    for (int i = 0; i < len; i++)
    {
        int remaining_val = target - nums[i];

        int c = store.count(remaining_val);
        if (c)
        {
            // Store the two indices (complement index and current index) in the result vector
            temp = {store[remaining_val], i};
            // Get runtime type information of temp vector for debugging
            const std::type_info &typeInfo = typeid(temp);
            // Get the demangled name of the type
            const char *name = typeInfo.name();
            // Return vector containing the two indices that sum to target
            return temp;
        }
        // Otherwise, store the current number and its index in the map
        store[nums[i]] = i;
    }

    // Return an empty vector if no solution is found
    return {};
}

int main()
{
    std::vector<int> test_vector = {2, 7, 11, 15};
    std::vector<int> result = twoSum(test_vector, 9);
    // Print the result
    for (int index : result)
    {
        std::cout << index << " ";
    }
    return 0;
}