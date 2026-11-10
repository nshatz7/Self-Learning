from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magaz_count = Counter(magazine)

        for letter in ransomNote:
            if letter not in magazine or ransom_count[letter] > magaz_count[letter]:
                return False
        
        return True
 