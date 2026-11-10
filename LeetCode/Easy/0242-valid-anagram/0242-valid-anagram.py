from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #immediately checks if same length, if not: not an anagram and doesnt do rest of function
            return False

        seent = Counter(t)
        seens = Counter(s)

        return seens == seent

        """
        for letter in t:
            if letter in s:
                if seens[letter] != seent[letter]:
                    return False
            else:
                return False    

        return True
        """