class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset=set()
        for i in range(len(nums)):
            print(myset)
            if nums[i] in myset:
                return nums[i]
            myset.add(nums[i])
            
        return 1
        