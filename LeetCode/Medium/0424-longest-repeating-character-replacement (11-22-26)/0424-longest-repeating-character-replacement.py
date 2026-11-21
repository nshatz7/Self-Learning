from collections import defaultdict #auto assigns default value to missing keys (preventing KeyError)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int) #frequency map
        left = 0
        max_freq = 0 #tracks highest count of any single character seen in the window
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1 #include the new right-handed character in window's frequency count
            max_freq = max(max_freq, counts[s[right]]) #update if bigger
            window_len = right - left + 1

            #window is invalid, so shift left forward by one
            if window_len - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            #recalculate window size in case left shifted and update max_len
            max_len = max(max_len, right - left + 1)
        
        return max_len


"""
Time complexity: 
    - O(n), where n is the length of the string s. Each character is added to the window once (right increases from 0 to n-1) and each character can be removed from the window at most once (left increases up to n). All operations inside the loop are O(1).
Space complexity: 
    - O(1) for the counts dictionary, since it stores a fixed number of character counts (at most the size of the alphabet, which is a constant factor with respect to n).
"""        
