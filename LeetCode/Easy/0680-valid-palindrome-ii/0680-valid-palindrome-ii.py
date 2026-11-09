class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.skipped_left(s[left+1: right+1], s, left, right)

        return True

    def skipped_left(self, restl, s, left, right):
        p1 = 0
        p2 = len(restl) - 1
        while p1 < p2:
            if restl[p1] == restl[p2]:
                p1 += 1
                p2 -= 1
            else:
                return self.skipped_right(s[left: right], s, left, right)

        return True

    def skipped_right(self, restr, s, left, right):
        p3 = 0
        p4 = len(restr) - 1
        while p3 < p4:
            if restr[p3] == restr[p4]:
                p3 += 1
                p4 -= 1
            else:
                return False

        return True


                


        