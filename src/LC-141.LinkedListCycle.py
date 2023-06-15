class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head
        while True:
            try:
                tortoise, hare = tortoise.next, hare.next.next
                if tortoise != hare:
                    continue
                else:
                    return True
            except:
                return False