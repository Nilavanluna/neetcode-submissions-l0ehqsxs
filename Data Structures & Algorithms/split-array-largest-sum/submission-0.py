class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # Helper: can we split into <= k subarrays with max sum <= limit?
        def can_split(limit):
            parts = 1
            curr = 0

            for n in nums:
                if curr + n > limit:
                    parts += 1
                    curr = n
                    if parts > k:
                        return False
                else:
                    curr += n

            return True

        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2

            if can_split(mid):
                high = mid   # try to lower the max sum
            else:
                low = mid + 1

        return low