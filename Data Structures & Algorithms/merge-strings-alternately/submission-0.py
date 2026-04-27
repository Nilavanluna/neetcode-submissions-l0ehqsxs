class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=min(word1,word2,key=len)
        res1=""
        for i in range(0,len(res)):
            res1+=word1[i]
            res1+=word2[i]
        i=i+1
        if res==word1:

            while i < len(word2):
                res1+=word2[i]
                i+=1
        else:
            while i < len(word1):
                res1+=word1[i]
                i+=1

        return res1