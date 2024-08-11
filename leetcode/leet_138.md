```python:leetcode/rough.py
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
```

### Explanation with Example

Let's break down the `copyRandomList` function step-by-step with an example.

#### Example Linked List
Consider a linked list with nodes having values `[1, 2, 3]` and random pointers `[None, 0, 1]`.

#### Step 1: Create a copy of each node and link them side-by-side
- **Initial List**: `1 -> 2 -> 3`
- **After Step 1**: `1 -> 1' -> 2 -> 2' -> 3 -> 3'`
  - Each original node is followed by its copy.

#### Step 2: Assign random pointers for the copy nodes
- **Original Random Pointers**: `1.random = None`, `2.random = 1`, `3.random = 2`
- **After Step 2**:
  - `1'.random = None`
  - `2'.random = 1'` (since `2.random` points to `1`, `2'.random` should point to `1'`)
  - `3'.random = 2'` (since `3.random` points to `2`, `3'.random` should point to `2'`)

#### Step 3: Restore the original list and extract the copy list
- **Before Step 3**: `1 -> 1' -> 2 -> 2' -> 3 -> 3'`
- **After Step 3**:
  - Restore original list: `1 -> 2 -> 3`
  - Extract copy list: `1' -> 2' -> 3'`

### Detailed Steps in Code

1. **Step 1: Create Copies**
   ```python
   current = head
   while current:
       new_node = Node(current.val, current.next, None)  # Create new node
       current.next = new_node  # Link new node after current
       current = new_node.next  # Move to the next original node
   ```

2. **Step 2: Assign Random Pointers**
   ```python
   current = head
   while current:
       if current.random:
           current.next.random = current.random.next  # Set random pointer for the copy
       current = current.next.next  # Move to the next original node
   ```

3. **Step 3: Restore and Extract**
   ```python
   current = head
   copy_head = head.next  # Head of the copied list
   while current:
       copy = current.next  # Copy node
       current.next = copy.next  # Restore original list
       if copy.next:
           copy.next = copy.next.next  # Link copy nodes
       current = current.next  # Move to the next original node
   ```

### Visualization

#### Initial List
```
1 -> 2 -> 3
```

#### After Step 1
```
1 -> 1' -> 2 -> 2' -> 3 -> 3'
```

#### After Step 2
```
1 -> 1' -> 2 -> 2' -> 3 -> 3'
     |         |         |
    None      1'        2'
```

#### After Step 3
- **Original List**: `1 -> 2 -> 3`
- **Copied List**: `1' -> 2' -> 3'`

