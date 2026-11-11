class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        stripped = s.split() #making list of all words 
        #bi-directional mapping
        p_to_s = {} 
        s_to_p = {}

        if len(stripped) != len(pattern): #case if they don't match up with the same length, must be false
            return False

        for char_p, char_s in zip(pattern, stripped):
            if char_p in p_to_s: 
                if p_to_s[char_p] != char_s: #if s does not match the pattern rule
                    return False
            else: #if it wasn't seen yet, add it to the rule
                p_to_s[char_p] = char_s

            if char_s in s_to_p:
                if s_to_p[char_s] != char_p: #bi-directional
                    return False
            else:
                s_to_p[char_s] = char_p

        return True #if loop went through without return false, must be true


"""
Time complexity: 
    - O(n), where n is the length of the pattern (and the number of words in s after splitting). Each of n iterations does O(1) work with dictionary lookups and insertions.

Space complexity: 
    - O(k), where k is the number of distinct tokens (distinct pattern characters plus distinct words). In the worst case, k is O(n). The additional space comes from the two dictionaries p_to_s and s_to_p and the list of words from splitting s.
"""
