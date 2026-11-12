class Solution:
    def romanToInt(self, s: str) -> int:
        test = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "I":
                test[i] = 1
            if s[i] == "V":
                test[i] = 5
            if s[i] == "X":
                test[i] = 10
            if s[i] == "L":
                test[i] = 50
            if s[i] == "C":
                test[i] = 100
            if s[i] == "D":
                test[i] = 500
            if s[i] == "M":
                test[i] = 1000
    
        answer = 0

        for y in range(len(test)):
            if y < len(test) - 1 and test[y] < test[y + 1]:
                answer -= test[y]
            else:
                answer+= test[y]


            
        return answer




        
