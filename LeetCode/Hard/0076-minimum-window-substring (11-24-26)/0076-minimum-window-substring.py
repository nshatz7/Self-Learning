from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)
        left = 0
        min_start, min_len = 0, float('inf') #"inf" just a palceholder for if it doesn't work
        
        for right, char in enumerate(s):
            # 1. Expand: If we still need this character, reduce total missing debt
            if need[char] > 0:
                missing -= 1
            need[char] -= 1  # Negative values indicate surplus characters
            
            # 2. Contract: Window is valid; shrink from left until it breaks
            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                    
                left_char = s[left]
                need[left_char] += 1
                
                # If need becomes positive, we just removed a mandatory character
                if need[left_char] > 0:
                    missing += 1
                left += 1
                
        return "" if min_len == float('inf') else s[min_start : min_start + min_len]


"""
Time complexity: 
    - O(n), where n is the length of s. Each character is added to the window once (right pointer) and removed at most once (left pointer), with constant-time updates to the counts.
Space complexity: 
    - O(k), where k is the number of distinct characters in t (at most O(1) with a fixed alphabet, but generally proportional to the size of the counter for t). The Counter need stores counts for characters in t and any extras encountered in s but tracked as negatives, so overall O(k) additional space.
"""
