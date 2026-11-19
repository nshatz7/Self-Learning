class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] #stores indices of days waiting for a warmer tempature

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp: #while the current tempature is warmer than previous
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            
            stack.append(curr_day) #push into stack to wait for a warmer day
        
        return answer
        