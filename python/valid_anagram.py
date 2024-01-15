class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two strings are anagrams (contain the same characters in the same frequencies).

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if the strings are anagrams, False otherwise.
        """

        # Base case: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create dictionaries to track character counts
        countS = {}  # Character counts for string s
        countT = {}  # Character counts for string t

        # Count character occurrences in each string
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1  # Increment count for character in s
            countT[t[i]] = countT.get(t[i], 0) + 1  # Increment count for character in t

        # Compare character frequencies
        for char in countS:
            if countS[char] != countT.get(char, 0):  # If count differs for any character, not anagrams
                return False

        # If all character frequencies match, strings are anagrams
        return True
