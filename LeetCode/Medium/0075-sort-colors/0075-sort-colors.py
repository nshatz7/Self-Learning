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

        