class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge alternately
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2