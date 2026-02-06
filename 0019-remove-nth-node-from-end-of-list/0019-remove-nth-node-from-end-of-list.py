class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast ahead n+1 steps
        for i in range(n + 1):
            fast = fast.next

        # Move both until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove node
        slow.next = slow.next.next

        return dummy.next
