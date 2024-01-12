class Solution {
  bool isPalindrome(String s) {
    String newS = s.toLowerCase().replaceAll(RegExp(r'[^a-z0-9]'), '');
    return newS == newS.split('').reversed.join('');
  }
}
