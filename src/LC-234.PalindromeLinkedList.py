# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        fast, slow = head, prev
        while slow:
            if slow.val != fast.val: return False
            slow, fast = slow.next, fast.next
        
        return True