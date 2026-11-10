from collections import Counter #turns the count of chars in the string into a hash map with how many times it appears

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #immediately checks if same length, if not: not an anagram and doesnt do rest of function
            return False

        return Counter(t) == Counter(s) #using counter module, returns true if they are the same, returns false if not
