class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if any(s1.isupper() for c in s1) or any(s2.isupper() for c in s2):
            return False

        d1="".join(sorted(s1))
        for i in range(0,len(s2)-k+1):
            sub=s2[i:i+k]
            if "".join(sorted(sub))==d1:
                return True

        return False