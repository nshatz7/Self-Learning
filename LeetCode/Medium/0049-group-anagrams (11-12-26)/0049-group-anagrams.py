class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {} #created a dictionary to store all the solutions matching the characters

        for word in strs:
            key = tuple(sorted(word)) #created a key that has all the values (tuple because you can't store a list as a dict key)
            if key in output:
                output[key].append(word)
            else:
                output.setdefault(key, []).append(word)
            
            output[key].sort() #sorting the values in the dictionary as instructed
        
        return list(output.values()) #returns the list of values


"""
Time complexity:
- Let n be the number of strings and L be the maximum length of a string.
- For each word, sorting costs O(L log L).
- Building/lookup in the dictionary is O(1) on average.
- Additionally, there is a per-key list sort after each insertion, which costs O(k log k) where k is the number of words sharing that key, but summing over all keys yields O(n log n) in the worst case when all words share the same key.
Overall, the dominant term is O(n * L log L) for sorting each word, plus at most O(n log n) for the per-group sorts. In practice, time is O(n * L log L).

Space complexity:
- The dictionary stores each word once in one of the groups, plus the keys, so O(n * L) for the total characters stored plus O(m) for the number of distinct anagram groups m (m ≤ n). The resulting output list also holds all words, contributing O(n * L) space. Therefore, O(n * L) extra space.
"""

        

        

                
            
                

        
        
