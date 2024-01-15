class Solution {
  // Function to check if two strings are anagrams (contain the same characters in the same frequencies)
  bool isAnagram(String s, String t) {
    // Base case: If lengths differ, they cannot be anagrams
    if (s.length != t.length) {
      return false;
    }

    // Create two maps to store character counts for each string
    final Map<String, int> countS = {}; // Map for string s
    final Map<String, int> countT = {}; // Map for string t

    // Count character occurrences in each string
    for (int i = 0; i < s.length; i++) {
      countS[s[i]] =
          1 + (countS[s[i]] ?? 0); // Increment count for character in s
      countT[t[i]] =
          1 + (countT[t[i]] ?? 0); // Increment count for character in t
    }

    // Compare character frequencies in both maps
    for (var c in countS.keys) {
      if (countS[c] != countT[c]) {
        // If count for any character differs, strings are not anagrams
        return false;
      }
    }

    // If all character frequencies match, strings are anagrams
    return true;
  }
}
