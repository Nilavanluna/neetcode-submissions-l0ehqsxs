class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps=ss=1
        l1=[]
        l2=[]
        l3=[]
        l1.append(1)
        l2.append(1)


        
        for i in range(0,len(nums)-1):
            ps=ps*nums[i]
            l1.append(ps)
           

           
        for j in range(len(nums)-1,0,-1):
            ss=ss*nums[j]
            l2.append(ss)
              
        k=0
        v=len(nums)-1
        print(l2)
        while k<len(nums):
            print(l1[k],l2[v])
            l3.append(l1[k]*l2[v])
          
            k+=1
            v-=1
        return l3

