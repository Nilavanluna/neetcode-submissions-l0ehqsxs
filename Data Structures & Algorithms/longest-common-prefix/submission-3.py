class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     res=""
     if len(strs)==1:
        return strs[0]
     for s in strs:
            if not s:
                return ""
     for i in range(0,len(strs[0])):
         res+=strs[0][i]
         for j in range (0,len(strs)):
            if strs[j].startswith(res):
                continue
            else:
                print("inside")
                return res[0:len(res)-1]

    
     return res