# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()  # Create a dummy head node for easier handling
        curr = dummyHead  # Pointer to the current node in the merged list

        while list1 and list2:  # Iterate while both lists have nodes
            if list1.val <= list2.val:  # Compare values and choose the smaller node
                curr.next = list1  # Append list1's current node
                list1 = list1.next  # Move to the next node in list1
            else:
                curr.next = list2  # Append list2's current node
                list2 = list2.next  # Move to the next node in list2
            curr = curr.next  # Advance the pointer in the merged list

        # Append any remaining nodes from either list (one might be empty)
        curr.next = list1 or list2

        return dummyHead.next  # Return the head of the merged list (excluding dummy)
        