class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} #creating a map to create a rule that s[0] = t[0] and so on
        t_to_s = {} #same thing bi-directional
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t: #if rule fails
                    return False
            else:
                s_to_t[char_s] = char_t #if its not stored, store it

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s: #if rule fails
                    return False
            else:
                t_to_s[char_t] = char_s #if its not stored, store it

        return True #loop goes through without failing it must be true


"""
Time complexity: 
    - O(n), where n is the length of the strings (since we process each position once).  
Space complexity: 
    - O(k), where k is the number of distinct characters encountered (in the worst case O(n) for the hash maps).
"""


                          
