//Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? mergeTwoLists(ListNode? list1, ListNode? list2) {
    // Create a dummy head node to simplify handling the beginning of the merged list
    ListNode dummyHead = ListNode();
    ListNode? curr =
        dummyHead; // Pointer to the current node in the merged list

    // Iterate through both lists while they have remaining nodes
    while (list1 != null && list2 != null) {
      // Compare values and choose the smaller node to append next
      if (list1.val <= list2.val) {
        curr!.next = list1; // Append list1's current node
        list1 = list1.next; // Move to the next node in list1
      } else {
        curr!.next = list2; // Append list2's current node
        list2 = list2.next; // Move to the next node in list2
      }
      curr = curr.next; // Advance the pointer in the merged list
    }

    // Append any remaining nodes from either list (one of them might be empty)
    if (list1 != null) {
      curr!.next = list1;
    } else if (list2 != null) {
      curr!.next = list2;
    }

    // Return the head of the merged list (excluding the dummy head)
    return dummyHead.next;
  }
}
