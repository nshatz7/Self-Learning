class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 
        while left < right: #while it doesn't cross the middle of the string
            if s[left] == s[right]: #if no changes need to be made
                left += 1
                right -= 1
            else:
                return self.skipped_left(s[left+1: right+1], s, left, right) #returns true or false for the left letter skipped (need right+1 though because when slicing, it doesn't include the end value which we need)

        return True #return true if the loop completed with never going through else (i.e. it didn't need to subtract)

    def skipped_left(self, restl, s, left, right):
        #make a new left and right value because the string "restl" is smaller
        p1 = 0
        p2 = len(restl) - 1
        while p1 < p2: 
            if restl[p1] == restl[p2]: #same argument as before but now with a shorter string
                p1 += 1
                p2 -= 1
            else:
                return self.skipped_right(s[left: right], s, left, right) #if it needed to subtract, but not subtract from the left: we check right

        return True #if the loop went through without touching the else statement, removing the left character was correct

    def skipped_right(self, restr, s, left, right): #do the same thing we did with skipped_left
        p3 = 0
        p4 = len(restr) - 1
        while p3 < p4:
            if restr[p3] == restr[p4]:
                p3 += 1
                p4 -= 1
            else:
                return False #this is the last argument so if it doesn't match, it's not a palindrome no matter what so it's going to return False to skipped_left, which then returns False to validPalindrome

        return True #if removing the right character was correct


    """
    Time complexity:
        - In the worst case, it compares characters while moving inward, and upon a mismatch, it recursively checks two possibilities: skipping the left character or skipping the right character. Each of those checks is essentially a linear scan of a substring.
        - In the worst case, this can lead to O(n) work for the initial pass plus up to two linear scans of substrings of size O(n), yielding O(n) time in typical two-pointer palindrome checks but potentially O(n^2) in worst cases where many recursive checks are triggered. Practically, since only one skip is allowed, the effective time remains close to O(n).

    Space complexity:
        - The function creates substrings (s[left+1:right+1], and subsequent substrings) which copy characters, leading to additional space usage. Each substring allocation is O(n) in size, and there can be a few such allocations in the worst path, giving O(n) auxiliary space per level of recursion.
        - Overall auxiliary space is O(n) due to substring copies, plus the implicit call stack depth which is O(1) since the implementation is iterative with a couple of helper methods, but substring allocations dominate.
    """

                


        
