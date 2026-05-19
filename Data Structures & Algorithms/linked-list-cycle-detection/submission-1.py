class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:      # same node encountered again
                return True
            visited.add(head)
            head = head.next

        return False