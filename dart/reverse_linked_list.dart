class ListNode {
  int? val;
  ListNode? next;

  ListNode([this.val, this.next]);
}

class Solution {
  ListNode? reverseList(ListNode? head) {
    ListNode? prev, curr;
    prev = null;
    curr = head;

    while (curr != null) {
      ListNode? nxt = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nxt;
    }

    return prev;
  }
}
