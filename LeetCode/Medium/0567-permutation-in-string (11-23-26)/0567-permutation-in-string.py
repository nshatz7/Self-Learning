class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        # Edge case: s2 cannot contain a permutation of s1 if s1 is longer
        if n1 > n2:
            return False

        # Fixed-size frequency arrays for 'a' through 'z'
        s1_count = [0] * 26
        window_count = [0] * 26

        # Step 1: Populate both frequency maps for the initial window of size n1
        for i in range(n1):
            s1_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        # Step 2: Count how many of the 26 characters currently have identical counts
        # (Note: characters absent from both strings have 0 == 0, which counts as a match)
        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        # Check if the initial window (indices 0 to n1 - 1) is already a valid permutation
        if matches == 26:
            return True

        # Step 3: Slide the fixed window one character at a time across s2
        left = 0
        for right in range(n1, n2):
            # --- Add incoming character at `right` ---
            r_idx = ord(s2[right]) - ord("a")
            window_count[r_idx] += 1

            if window_count[r_idx] == s1_count[r_idx]:
                # Adding this character resolved a frequency mismatch
                matches += 1
            elif window_count[r_idx] == s1_count[r_idx] + 1:
                # Adding this character broke a match that existed right before the increment
                matches -= 1

            # --- Remove outgoing character at `left` ---
            l_idx = ord(s2[left]) - ord("a")
            window_count[l_idx] -= 1

            if window_count[l_idx] == s1_count[l_idx]:
                # Removing this character resolved a frequency mismatch
                matches += 1
            elif window_count[l_idx] == s1_count[l_idx] - 1:
                # Removing this character broke a match that existed right before the decrement
                matches -= 1

            # Advance `left` so the window remains [left, right] of length n1
            left += 1

            # Short-circuit immediately as soon as all 26 character counts match
            if matches == 26:
                return True

        return False


"""
Time complexity: 
    - O(n2), where n2 is the length of s2. Each position in s2 is visited once for the sliding window, with a constant amount of work per step. The initial counting is O(n1), and the per-step updates are O(1).
Space complexity: 
    - O(1) extra space, specifically O(1) for the two fixed-size frequency arrays of length 26, plus a few scalar variables.
"""
