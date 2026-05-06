class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        ans=l
        def canship(mid):
            nd=1
            curr=0
            for w in weights:
                if curr+w>mid:
                    curr=0
                    nd+=1
                curr+=w
            print(nd,mid)
            return nd<=days
        while l<=r:
            mid=(l+r)//2
            if canship(mid):
                r=mid-1
                ans=mid
            else:
                l=mid+1  


        return ans 
                 