from collections import Counter #turns the count of chars in the string into a hash map with how many times it appears

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #immediately checks if same length, if not: not an anagram and doesnt do rest of function
            return False

        return Counter(t) == Counter(s) #using counter module, returns true if they are the same, returns false if not

    #Time complexity: O(n) where n is the length of the strings (s and t). We build two Counter objects each in O(n) time, and comparison of two Counters is O(k) where k is the number of distinct characters (<= n). Overall O(n).

    #Space complexity: O(k) extra space, where k is the number of distinct characters in the inputs (worst case O(n)). The two Counter objects store character frequencies. There is no other significant extra space.
