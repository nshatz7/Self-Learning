class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]] #buffer variable

        for i in range(1, len(intervals)): #starting at the tuple ahead of the buffer so we don't repeat
            if merged[-1][1] >= intervals[i][0]: #using the tail of buffer (most recent added) end value overlapping with intervals[i] end value
                merged[-1][1] = max(merged[-1][1], intervals[i][1]) #adds the largest end value
            else: #if they don't overlap, add intervals[i] tuple to buffer
                merged.append(intervals[i])
        
        return merged #return buffer at the end


        