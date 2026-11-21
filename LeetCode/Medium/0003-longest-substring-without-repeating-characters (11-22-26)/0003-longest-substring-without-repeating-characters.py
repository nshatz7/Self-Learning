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


"""
Time complexity: 
    - O(n), where n is the length of the string. Each character is visited once by the right pointer and each dictionary operation is O(1) on average.
Space complexity: 
    - O(min(n, m)) where m is the size of the character set. In the worst case the last_seen dictionary stores up to n distinct characters, but it cannot exceed the number of possible characters in the input alphabet.
"""     
