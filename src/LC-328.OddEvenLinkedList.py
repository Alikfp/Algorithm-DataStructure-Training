class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next) or (not head.next.next) :
            return head
        
        o, e = head, head.next
        fst_even = head.next
        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next

            o = o.next
            e = e.next
        o.next = fst_even
        return head