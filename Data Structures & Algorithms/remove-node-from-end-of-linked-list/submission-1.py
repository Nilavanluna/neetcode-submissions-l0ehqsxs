class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        # you asked to KEEP this condition
        if count == n:
            return head.next   # return new head instead of empty list

        bnd = count - n - 1     # <-- You MUST compute bnd

        mov = head
        while mov:
            if bnd == 0:
                mov.next = mov.next.next
                break
                        # <-- stop after removal
            bnd -= 1
            mov = mov.next

        return head