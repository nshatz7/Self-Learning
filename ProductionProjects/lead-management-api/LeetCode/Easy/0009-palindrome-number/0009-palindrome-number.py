class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = False
        for y in range(len(str(x))):
            test1 = str(x)[y]
            test2 = str(x)[-1-y]

            if test1 == "-":
                answer = False
                return answer

            if test1 == test2:
                answer = True
            else:
                answer = False
                return answer
        
        return answer