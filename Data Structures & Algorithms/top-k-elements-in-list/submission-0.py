from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq=Counter(nums)
       i=0
       res=[]
       for key,value in freq.most_common():
          if i<k:
            print(key)
            res.append(key)
            i+=1
       print(freq)
       return res 
