class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #return Counter(magazine) >= Counter(ransomNote)
        count = [0] * 26 #intializes a fixed-size array (all lowercase)

        for letter in magazine: #checking to see how many times each letter in magazine appears
            index = ord(letter) - ord('a') #index of the letter in the count array in alphabetical order('a' = 0, 'b' = 1), -ord('a') because that sets every character that subtracts every characters ASCII from the ASCII of 'a', making a = 0, b = 1, and so on
            count[index] += 1 #adds one to the array in that index
        
        for letter in ransomNote:
            index = ord(letter) - ord('a')
            count[index] -= 1 #removing one from the count so we know that letter was used in ransomNote 1x
            if count[index] < 0: #if its less than zero, that means the ransom note used more of a letter than the magazine had
                return False
        
        return True #if it got through the whole second loop without returning false, then it has to be true

    
    



            

            

 