
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pref = ListNode()
        pref_p = pref
        curr = dummy
        while curr.next:
            if curr.next.val < x:
                tmp = curr.next.next
                pref_p.next = curr.next
                pref_p = pref_p.next
                pref_p.next = None
                curr.next = tmp
            else:
                curr = curr.next
        pref_p.next = dummy.next
        return pref.next
