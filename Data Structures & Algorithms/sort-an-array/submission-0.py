class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
         return nums
        mid=len(nums)//2
        lef=nums[:mid]
        rig=nums[mid:]

        left_sort=self.sortArray(lef)
        right_sort=self.sortArray(rig)

        return self.merge(left_sort,right_sort)
    def merge(self,left,right):
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        

        while i<len(left):
                result.append(left[i]) 
                i+=1
        while j<len(right):
                result.append(right[j]) 
                j+=1
        return result
             
        