# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        tail = None

        while head:
            temp = head
            head = head.next
            temp.next = tail
            tail = temp
        
        return tail