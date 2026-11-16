class Solution:
    def sortColors(self, nums: list[int]) -> None:
        #add starting values for dutch national flag algorithm
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high: #once mid crosses high the unknown zone vanishes and the array is sorted
            #closing in on the unknown zone with case handling
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low] #swapping
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else: #nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high] #swapping
                high -= 1


"""
Time complexity: 
    - O(n), where n is the length of nums. Each element is swapped at most a couple of times and the pointers low, mid, high traverse the array once.

Space complexity: 
    - O(1) extra space. It uses only a few integer variables and swaps in place.
"""

        
