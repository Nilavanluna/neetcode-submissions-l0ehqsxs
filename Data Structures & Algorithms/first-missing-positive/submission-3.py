class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i=0
        for i in range(len(nums)):
            if nums[i]>0:
                break
        if nums[i]>1:
            return 1
        print(i)
        for i in range(len(nums)-1):
            
            if nums[i]== (nums[i+1]):
                continue
            elif nums[i]+1>0 and nums[i]+1 != (nums[i+1]):
                return nums[i]+1
        return nums[len(nums)-1]+1 if nums[len(nums)-1]>0 else 1
