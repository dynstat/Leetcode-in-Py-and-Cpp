#include <iostream>
// Definition for singly-linked list.
struct ListNode
{
    int val;        // Value of the node
    ListNode *next; // Pointer to the next node in the list

    // Default constructor initializes the node with value 0 and next pointer as nullptr
    ListNode() : val(0), next(nullptr) {}

    // Constructor initializes the node with a given value and next pointer as nullptr
    ListNode(int x) : val(x), next(nullptr) {}

    // Constructor initializes the node with a given value and a given next pointer
    ListNode(int x, ListNode *nextNode) : val(x), next(nextNode) {}
};

class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *dummy = new ListNode(0, head);

        ListNode *sp = dummy;
        ListNode *fp = dummy;
        while (n--)
        {
            std::cout << fp->val;
            fp = fp->next; // assuming the value of n is less than the total length of the linked list, hence not handling that case.
        }
        while (fp->next != nullptr)
        {
            sp = sp->next;
            fp = fp->next;
        }
        sp->next = sp->next->next;
        return dummy->next;
    }
};

int main()
{
    // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode *head = nullptr;
    ListNode node1(1);
    ListNode node2(2);
    ListNode node3(3);
    ListNode node4(4);
    ListNode node5(5);

    // Link the nodes together accordingly
    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node5;

    // Set the head pointer to the first node
    head = &node1;

    // Remove the 2nd node from the end
    Solution s;
    head = s.removeNthFromEnd(&node1, 2);

    // Print the linked list
    while (head != nullptr)
    {
        std::cout << head->val << " ";
        head = head->next;
    }
}