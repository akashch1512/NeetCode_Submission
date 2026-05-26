# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        main = head
        def rev_ll(head):
            res = None
            temp = 0
            while head:
                temp = head.next
                head.next = res 
                res = head
                head = temp
            
            return res
            
        # Finding the length of linked List
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Dividing the Linked List
        l = 0
        curr = head
        # Even Total Elements
        if length % 2 == 0:
            while l < (length // 2 - 1):
                curr = curr.next
                l += 1
        
        # Odd Total Elements
        else:
            while l < (length // 2):
                curr = curr.next
                l += 1

        # revsered linked list of insersion
        strt = rev_ll(curr)
        
        # Inserting Nodes at Extact Point
        curr = head
        ulat = strt

        while curr and ulat:
            temp = curr.next
            temp2 = ulat.next

            curr.next = ulat
            ulat.next = temp

            curr = temp
            ulat = temp2