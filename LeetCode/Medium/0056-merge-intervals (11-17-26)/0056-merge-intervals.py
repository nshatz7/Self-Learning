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


"""
Time complexity: 
    - O(n log n) due to sorting the intervals. The merge pass is O(n).

Space complexity: 
    - O(1) extra space if we modify in place (besides the output list). Since the code builds the merged list in place using the input list and only stores the result in merged, the extra space is O(1) beyond the output. If we count the output, total space is O(n).
"""

        
