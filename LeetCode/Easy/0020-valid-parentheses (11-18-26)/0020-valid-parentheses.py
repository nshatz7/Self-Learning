class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            match char:
                case '(' | '{' | '[': #adding the first parenthesis match to the stack
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(': #if the last value was not the mathing parenthesis or if the stack is empty, must return false
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False

        return len(stack) == 0 #if every item was popped, it's true. If not, false


"""
Time complexity: 
    - O(n), where n is the length of the string. Each character is pushed or popped from the stack at most once.

Space complexity: 
    - O(n) in the worst case, due to the stack storing up to n characters (e.g., when the string consists of only opening brackets).
"""


    
        
