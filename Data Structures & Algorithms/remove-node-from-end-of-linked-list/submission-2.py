# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        index = 0
        
        while fast:
            if index > n:
                slow = slow.next
            index += 1
            fast = fast.next
            
        
        if n < index:
            slow.next = slow.next.next
        else:
            head = head.next
        
        return head