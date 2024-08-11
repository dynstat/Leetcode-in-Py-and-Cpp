# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return (
            f"({str(id(self))[-1:-4:-1]})[{self.val}, {self.random.val}]"
            if self.random
            else f"({str(id(self))[-1:-4:-1]})[{self.val}, None]"
        )


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create a copy of each node and link them side-by-side in a single list.
        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the copy nodes.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Restore the original list, and extract the copy list.
        current = head
        copy_head = head.next
        while current:
            copy = current.next
            current.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            current = current.next

        return copy_head


# Test and print results
if __name__ == "__main__":
    # Create test cases
    def create_linked_list(values, random_indices):
        nodes = [Node(val) for val in values]
        for i, node in enumerate(nodes):
            if i < len(nodes) - 1:
                node.next = nodes[i + 1]
            if random_indices[i] is not None:
                node.random = nodes[random_indices[i]]
        return nodes[0] if nodes else None

    # Test case 1: Simple list with random pointers
    head1 = create_linked_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])

    # Test case 2: List with self-referencing random pointers
    head2 = create_linked_list([1, 2, 3], [1, 2, 0])

    # Test case 3: Empty list
    head3 = None

    # Test case 4: Single node with self-referencing random pointer
    head4 = create_linked_list([1], [0])

    solution = Solution()

    # Helper function to print the linked list
    def print_linked_list(head):
        current = head
        while current:
            random_val = current.random.val if current.random else None
            print(f"[{current.val}, {random_val}]", end=" -> ")
            current = current.next
        print("None")

    # Test and print results
    for i, test_case in enumerate([head1, head2, head3, head4], 1):
        print(f"\nTest case {i}:")
        print("Original list:")
        print_linked_list(test_case)

        copied = solution.copyRandomList(test_case)

        print("Copied list:")
        print_linked_list(copied)
