from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)   # FIX 1: correct default factory
        
        for s in strs:
            freq = [0] * 26              # count array
            
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            
            key = tuple(freq)            # FIX 2: must be inside loop
            anagram_map[key].append(s)
        
        return list(anagram_map.values())  # FIX 3: return only values