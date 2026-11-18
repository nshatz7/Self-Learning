class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = [] #explicit stack

        for char in tokens:
            if char in {"+", "-", "*", "/"}: #if char is an operator
                number2 = int(stack.pop()) #pop the last number which when using pop it reverses, so the first pop is second number in equation
                number1 = int(stack.pop())

                #operations for each operator that is possible
                if char == '+':
                    added = number1 + number2
                    stack.append(added)
                elif char == '-':
                    added = number1 - number2
                    stack.append(added)
                elif char == '*':
                    added = number1 * number2
                    stack.append(added)
                else:
                    added = number1 / number2
                    stack.append(added)  
            else: #means that the char is a number, so append it to the stack so we can pop it on the next operation
                stack.append(char)
        
        return int(stack[0]) #returns the only value in stack without "[]" and without "''"


"""
Time complexity: 
    - O(n), where n is the number of tokens. Each token is pushed once and each operator pops two items and pushes one result, resulting in linear total operations.

Space complexity: 
    - O(n) in the worst case, due to the stack storing up to n tokens (e.g., when many numbers appear before any operator). The actual max size is proportional to the input, not the computed results.
"""
        
