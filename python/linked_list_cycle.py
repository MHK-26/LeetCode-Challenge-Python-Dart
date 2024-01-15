class Solution(object):
    def hasCycle(self, head):
        """
        Determines if a linked list contains a cycle (loop).

        Args:
            head: The head of the linked list.

        Returns:
            True if the linked list has a cycle, False otherwise.
        """

        slow = fast = head  # Initialize two pointers at the head

        while fast and fast.next:  # Iterate while both pointers are valid
            slow = slow.next  # Move slow pointer one step at a time
            fast = fast.next.next  # Move fast pointer two steps at a time

            if slow == fast:  # If pointers meet, there's a cycle
                return True

        return False  # If pointers never meet, there's no cycle