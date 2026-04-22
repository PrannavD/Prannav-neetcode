class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)       # create dummy
        dummy.next = head         # connect to list

        fast = dummy              # both start at dummy
        slow = dummy

        for _ in range(n + 1):   # PHASE 2: move fast alone n+1 steps
            fast = fast.next

        while fast:               # PHASE 3: move both together
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # delete target

        return dummy.next           # return actual head