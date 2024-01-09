class Solution {
  bool isAnagram(String s, String t) {
    if (s.length != t.length) {
      return false;
    }

    final Map<String, int> countS = {};
    final Map<String, int> countT = {};

    for (int i = 0; i < s.length; i++) {
      countS[s[i]] = 1 + (countS[s[i]] ?? 0);
      countT[t[i]] = 1 + (countT[t[i]] ?? 0);
    }

    for (var c in countS.keys) {
      if (countS[c] != countT[c]) {
        return false;
      }
    }

    return true;
  }
}
