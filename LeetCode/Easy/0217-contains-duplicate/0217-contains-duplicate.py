class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set() #checking if item exists and keeping it in O(1) constant
        for number in nums: #this makes time: o(n) linear
            if number in seen:
                return True #automatically break the loop (saving time and returning the answer)
            seen.add(number) #adds that number to seen so it can do the for loop on the next passes (also never returns true on first loop because nothing is in seen yet)

        return False #returns false because if the if statement never got passed, it never returned true so fallsback to false if never returned true

        #Time Complexity: o(n) linear because one for loop in the code automatically makes it o(n), two makes it o(n^2)

        """
        what I learned:
        - Using two nested loops results in a time complexity of o(n^2). This is an issue because for large data sets this takes a long amount of time for something simple.
            -To fix this, use Python data structures that let you test for exisistence with o(1) constant:
                - set (checks if an item exists, what I used in this problem)
                - dict (looks up a value via a key)
        """

        

 
        