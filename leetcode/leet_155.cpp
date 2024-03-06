// # 155. Min Stack
// # Medium
// # 11.6K
// # 735
// # Companies
// # Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// # Implement the MinStack class:

// # MinStack() initializes the stack object.
// # void push(int val) pushes the element val onto the stack.
// # void pop() removes the element on the top of the stack.
// # int top() gets the top element of the stack.
// # int getMin() retrieves the minimum element in the stack.
// # You must implement a solution with O(1) time complexity for each function.

// # Example 1:

// # Input
// # ["MinStack","push","push","push","getMin","pop","top","getMin"]
// # [[],[-2],[0],[-3],[],[],[],[]]

// # Output
// # [null,null,null,null,-3,null,0,-2]

// # Explanation
// # MinStack minStack = new MinStack();
// # minStack.push(-2);
// # minStack.push(0);
// # minStack.push(-3);
// # minStack.getMin(); // return -3
// # minStack.pop();
// # minStack.top();    // return 0
// # minStack.getMin(); // return -2

// # ````````````````````````````````

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class MinStack
{
public:
    vector<int> s;
    vector<int> min_s;
    int min_val;

    MinStack() {}

    void push(int val)
    {
        if (s.empty())
        {
            min_val = val;
        }
        if (min_val >= val)
        {
            min_val = val;
        }
        s.push_back(val);
        min_s.push_back(min_val);
    }

    void pop()
    {
        if (!s.empty())
        {
            s.pop_back();
            min_s.pop_back();
        }
        if (!min_s.empty())
        {
            min_val = min_s.back();
        }
    }

    int top()
    {
        return s.back();
    }

    int getMin()
    {
        return min_s.back();
    }
};

int main()
{
    // ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
    // [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]

    MinStack *minStack = new MinStack();
    minStack->push(-10);
    cout << "Pushed -10\n";

    minStack->push(14);
    cout << "Pushed 14\n";

    cout << "Current Min: " << minStack->getMin() << endl; // Should be -10

    cout << "Current Min: " << minStack->getMin() << endl; // Should still be -10

    minStack->push(-20);
    cout << "Pushed -20\n";

    cout << "Current Min: " << minStack->getMin() << endl; // Should be -20

    cout << "Current Min: " << minStack->getMin() << endl; // Should still be -20

    cout << "Top element: " << minStack->top() << endl; // Should be -20

    cout << "Current Min: " << minStack->getMin() << endl; // Should still be -20

    minStack->pop();
    cout << "Popped top element\n";

    minStack->push(10);
    cout << "Pushed 10\n";

    minStack->push(-7);
    cout << "Pushed -7\n";

    cout << "Current Min: " << minStack->getMin() << endl; // Should be -10

    minStack->push(-7);
    cout << "Pushed -7\n";

    minStack->pop();
    cout << "Popped top element\n";

    cout << "Top element: " << minStack->top() << endl; // Should be -7

    cout << "Current Min: " << minStack->getMin() << endl; // Should be -10

    minStack->pop();
    cout << "Popped top element\n";

    delete minStack; // Don't forget to free the allocated memory
}
