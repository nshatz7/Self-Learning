from collections import Counter #Counter gives all the elements in the string and their count as a hash map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) #if the elements and or their count don't agree, prints false (or the other way around)


"""
Time complexity: 
    - O(n), where n is the length of the strings combined (specifically, O(len(s) + len(t))). Counter builds frequency maps for both strings in linear time.

Space complexity: 
    - O(k), where k is the number of distinct characters in the strings (in the worst case O(n) if all characters are unique). Counter stores the frequency for each character, so extra space scales with the alphabet size actually used.
"""