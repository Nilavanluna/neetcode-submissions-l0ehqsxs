import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        s=s.lower()
        end=len(s)-1

        print(s)
        while start<end:
       
            if s[start]==s[end]:
                start+=1
                end-=1        
            else:
                return False
        return True