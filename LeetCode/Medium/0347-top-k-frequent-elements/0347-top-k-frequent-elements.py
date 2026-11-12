from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [key for key, count in Counter(nums).most_common(k)]

        
        