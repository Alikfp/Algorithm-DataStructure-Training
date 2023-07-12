# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self,head: Optional[ListNode],left: int,right: int) -> Optional[ListNode]:
        if left == right : return head
        dummy = ListNode(next=head)
        h = dummy
        for _ in range(left-1):
            h = h.next
        
        curr = h.next
        nxt = h.next.next

        for _ in range(right-left):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        
        h.next.next = nxt
        h.next = curr
        
        return dummy.next
        