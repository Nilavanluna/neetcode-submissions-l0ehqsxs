class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            # If we find a duplicate, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the current character and update the maximum length
            char_set.add(s[r])
            res = max(res, r - l + 1)
            
        return res