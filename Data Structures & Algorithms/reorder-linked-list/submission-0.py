class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ── STEP 1: Find Middle ──────────────────────────
        slow, fast = head, head                  # Line 1

        while fast and fast.next:                # Line 2
            slow = slow.next                     # Line 3
            fast = fast.next.next                # Line 4

        # ── STEP 2: Reverse Second Half ──────────────────
        prev = None                              # Line 5
        curr = slow.next                         # Line 6
        slow.next = None                         # Line 7

        while curr:                              # Line 8
            next_node = curr.next                # Line 9
            curr.next = prev                     # Line 10
            prev = curr                          # Line 11
            curr = next_node                     # Line 12

        # ── STEP 3: Merge Two Halves ─────────────────────
        first, second = head, prev               # Line 13

        while second:                            # Line 14
            tmp1 = first.next                    # Line 15
            tmp2 = second.next                   # Line 16

            first.next = second                  # Line 17
            second.next = tmp1                   # Line 18

            first = tmp1                         # Line 19
            second = tmp2                        # Line 20