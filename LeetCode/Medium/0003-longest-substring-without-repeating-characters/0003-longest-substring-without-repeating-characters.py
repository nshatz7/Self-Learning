class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {} #intializing dictionary so we can teleport left (unlike a set)
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            #only jump if the duplicate is INSIDE our current window
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1 #directly passes the previous occurence to remove duplicates
            
            last_seen[char] = right #update the characters latest index to the current position
            max_len = max(max_len, right - left + 1) #calculate current window size and update if bigger

        return max_len
        