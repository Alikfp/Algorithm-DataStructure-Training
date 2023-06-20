# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        hold = 0
        dummy_head = ListNode()
        curr = dummy_head
        while p1 or p2 or hold:
            num1=num2=0
            if p1:
                num1 = p1.val
                p1 = p1.next
            if p2:
                num2 = p2.val
                p2 = p2.next

            sum_= (num1+num2+hold)%10
            hold = (num1+num2+hold)//10 
            curr.next = ListNode(sum_)
            curr = curr.next

        return dummy_head.next
            
