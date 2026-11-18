class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for char in tokens:
            if char in {"+", "-", "*", "/"}:
                number2 = int(stack.pop())
                number1 = int(stack.pop())

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
            else:
                stack.append(char)
        
        return int(stack[0])


        