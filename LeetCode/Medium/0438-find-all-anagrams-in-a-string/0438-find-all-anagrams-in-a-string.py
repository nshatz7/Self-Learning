class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ns, np = len(s), len(p)

        # Edge case: s cannot contain any anagram of p if p is longer
        if np > ns:
            return []

        # Fixed-size frequency arrays for 'a' through 'z'
        p_count = [0] * 26
        window_count = [0] * 26

        # Step 1: Populate both frequency maps for the initial window of size np
        for i in range(np):
            p_count[ord(p[i]) - ord("a")] += 1
            window_count[ord(s[i]) - ord("a")] += 1

        # Step 2: Count how many of the 26 characters currently have identical counts
        matches = 0
        for i in range(26):
            if p_count[i] == window_count[i]:
                matches += 1

        # Record index 0 if the very first window is an anagram of p
        result = []
        if matches == 26:
            result.append(0)

        # Step 3: Slide the fixed window across the entire string s
        left = 0
        for right in range(np, ns):
            # --- Add incoming character at `right` ---
            r_idx = ord(s[right]) - ord("a")
            window_count[r_idx] += 1

            if window_count[r_idx] == p_count[r_idx]:
                # Frequency now matches p_count
                matches += 1
            elif window_count[r_idx] == p_count[r_idx] + 1:
                # Frequency exceeded p_count by 1, breaking a previous match
                matches -= 1

            # --- Remove outgoing character at `left` ---
            l_idx = ord(s[left]) - ord("a")
            window_count[l_idx] -= 1

            if window_count[l_idx] == p_count[l_idx]:
                # Frequency now matches p_count
                matches += 1
            elif window_count[l_idx] == p_count[l_idx] - 1:
                # Frequency dropped below p_count by 1, breaking a previous match
                matches -= 1

            # Advance `left` FIRST so it points to the start of the updated window [left, right]
            left += 1

            # Collect the starting index and keep sliding (do not return early)
            if matches == 26:
                result.append(left)

        return result
