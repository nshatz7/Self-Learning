from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [key for key, count in Counter(nums).most_common(k)] #gets the key from counter(nums) and .most_common(k) gets the top k elements (for ex: k = 2, top 2 elements)


"""
Time complexity: 
    - O(n log k) on average due to selecting the top k elements from the Counter. Building the counter is O(n). If implemented as a full sort of all unique elements, it would be O(m log m) where m is the number of unique elements, but most_common(k) typically uses a heap to achieve O(n log k) overall for the input size n.
Space complexity: 
    - O(m) for storing the frequencies of the m unique elements, plus O(k) for the output. In total, O(m) auxiliary space.
"""
        
        
