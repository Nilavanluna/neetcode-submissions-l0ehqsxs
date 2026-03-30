class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
     nums.sort()
     res=[]
     c=len(nums)/3
     v=0
     for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            v+=1
        else:
            if v+1>c:
                res.append(nums[i])
            v=0
     if  v+1>c:
        res.append(nums[len(nums)-1])
     return res
        