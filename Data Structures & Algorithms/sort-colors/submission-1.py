class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        r=len(nums)-1
        while mid<=r:
         if nums[mid]==0:
            k=nums[mid]
            nums[mid]=nums[low]
            nums[low]=k
            mid+=1
            low+=1
        
         elif nums[mid]==1:
            mid+=1
         else:
            k=nums[mid]
            nums[mid]=nums[r]
            nums[r]=k
        
            r-=1
   
