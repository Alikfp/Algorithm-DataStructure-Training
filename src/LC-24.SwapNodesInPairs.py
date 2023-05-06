# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pending, curr = dummy, head

        while curr and curr.next:
            nxt_pair = curr.next.next
            snd = curr.next


            snd.next = curr
            curr.next = nxt_pair
            pending.next = snd
            
            pending = curr
            curr = nxt_pair

        
        return dummy.next



            
