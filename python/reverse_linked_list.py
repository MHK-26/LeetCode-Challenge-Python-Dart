class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in place.

        Args:
            head: The head of the linked list to be reversed.

        Returns:
            The head of the reversed linked list.
        """

        prev = None  # Pointer to the previous node (starts as None)
        curr = head  # Pointer to the current node (starts at the head)

        while curr:  # Iterate through the list until reaching the end
            nxt = curr.next  # Store the next node before reversing links
            curr.next = prev  # Reverse the link of the current node
            prev = curr  # Move prev to the current node for the next iteration
            curr = nxt  # Move curr to the next node

        return prev  # The new head of the reversed list is the last node in the original list
