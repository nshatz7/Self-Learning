class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged = [] #buffer variable
        i = 0
        n = len(intervals)

        #adding all intervals that end before "newInterval" starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        #merging all overlapping intervals into "newInterval"
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval) #adding "newInterval" to buffer
        
        #adding intervals that start after "newInterval"
        while i < n: 
            merged.append(intervals[i])
            i += 1

        return merged


"""
Time complexity: 
    - O(n), where n is the number of input intervals. Each interval is visited a constant number of times: once in the initial pass, once in the merging pass (if overlapping), and once in the final pass.

Space complexity: 
    - O(n), for storing the resulting merged array. In the worst case, all input intervals are kept (no overlaps with the newInterval), producing a result of size n or n+1.
"""


        

        
        
