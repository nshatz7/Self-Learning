class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        stripped = s.split()
        p_to_s = {}
        s_to_p = {}

        if len(stripped) != len(pattern):
            return False

        for char_p, char_s in zip(pattern, stripped):
            if char_p in p_to_s:
                if p_to_s[char_p] != char_s:
                    return False
            else:
                p_to_s[char_p] = char_s

            if char_s in s_to_p:
                if s_to_p[char_s] != char_p:
                    return False
            else:
                s_to_p[char_s] = char_p

        return True
