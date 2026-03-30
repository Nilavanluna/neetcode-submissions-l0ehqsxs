from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        prefix_sum = 0
        count = 0
        
        for x in nums:
            prefix_sum += x
            
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
                
            prefix_count[prefix_sum] += 1
            
        return count



