class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res=[]
        for n1 in nums1:
            res.append(n1)
        
        for n2 in nums2:
            res.append(n2)
        
        res.sort()
        mid=len(res)//2
        if len(res)%2!=0:
            return res[mid]
            


        print(res)
        return (res[mid]+res[mid-1])/2

        