class MinStack:

    def __init__(self):
        self.stack = [] #stores tuple of (value, current_min)
        
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            current_min = min(value, self.stack[-1][1]) #comparing value against current states min
            self.stack.append((value, current_min))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Time complexity:
- push: O(1) to compute min and append.
- pop: O(1) to remove the top element.
- top: O(1) to read the top value.
- getMin: O(1) to read the current minimum.

Space complexity:
- O(n) extra space to store n elements, each as a tuple (value, current_min). The space overhead per element is constant, so overall O(n).
"""
