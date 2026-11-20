class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        #precomputing target sum to avoid divison
        target = threshold * k

        #building the intial window and checking before sliding
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0

        #sliding window and incrementing count whenever the condition is true
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]
            if window_sum >= target:
                count += 1
        
        return count


"""
Time Complexity: 
    - O(k) for computing the initial window sum 
    - O(1) per step when sliding across the remaining n - k elements
    - O(n) total time
Space Complexity:
    - O(1) beyond a few scalar variables
"""


        
