class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            # Swapping
            prev.next = b
            a.next = b.next
            b.next = a

            # Move prev forward
            prev = a

        return dummy.next