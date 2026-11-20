class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        #computing first window's sum (indices 0 to k-1)
        window_sum = sum(nums[:k])

        #Initalizing max_sum to the first window (handles negative arrays)
        max_sum = window_sum

        #sliding windows and updating max_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k] #sliding window one step at a time from index k to n-1
            if window_sum > max_sum:
                max_sum = window_sum #updating max if the next window is larger than previous
            
        return max_sum / k #dividing at end avoids unnecessary floating-point division on every iteration


"""
Time complexity: 
    - O(n), where n is the length of nums. It computes the initial sum in O(k) and then slides the window across the remaining n-k elements with O(1) work per step, totaling O(n).
Space complexity: 
    - O(1), aside from a few scalar variables. It uses constant extra space.
"""
