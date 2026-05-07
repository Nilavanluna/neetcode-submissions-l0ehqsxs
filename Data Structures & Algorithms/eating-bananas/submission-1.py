import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      l,r=1,max(piles)
      ans=l
      def caneat(mid):
        nd=0
        temp=mid
        
        for p in piles:
            if mid>=p:
                nd+=1
            else: 
                    
                
                    nd+=math.ceil(p/mid)
                    
            
       
        return nd<=h
       
      while l<=r:
        mid=(l+r)//2
        
        if caneat(mid):
            r=mid-1
            ans=mid
        else:
            l=mid+1
                

      return ans
        