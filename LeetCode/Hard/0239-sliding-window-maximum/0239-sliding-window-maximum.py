from collections import deque #importing deque: double-ended queue
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices; values are strictly decreasing
        result = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that have fallen out of the left side of the window
            if dq and dq[0] <= i - k:
                dq.popleft()
                
            # 2. Maintain monotonic decreasing property: purge smaller elements from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()
                
            # 3. Add current index
            dq.append(i)
            
            # 4. Once the first window of size k is formed, record the front element
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result