class ListNode {
  int? val;
  ListNode? next;

  ListNode([this.val, this.next]);
}

class Solution {
  // Method to reverse a linked list.
  ListNode? reverseList(ListNode? head) {
    // Declare two pointers, prev and curr.
    ListNode? prev, curr;
    prev =
        null; // Initialize prev to null as there's no node before the head initially.
    curr = head; // Initialize curr to the head of the linked list.

    // Iterate through the linked list.
    while (curr != null) {
      // Save the reference to the next node.
      ListNode? nxt = curr.next;

      // Reverse the link direction.
      curr.next = prev;

      // Move prev and curr pointers to the next nodes.
      prev = curr;
      curr = nxt;
    }

    // The new head of the reversed linked list is the last node.
    return prev;
  }
}
