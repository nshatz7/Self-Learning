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
            
                


    
        