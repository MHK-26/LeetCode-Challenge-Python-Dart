class Solution {
  // Function to check if a string is a palindrome (reads the same backward and forward)
  bool isPalindrome(String s) {
    // Preprocessing:
    String newS =
        s.toLowerCase(); // Convert to lowercase for case-insensitive comparison
    newS = newS.replaceAll(
        RegExp(r'[^a-z0-9]'), ''); // Remove non-alphanumeric characters

    // Palindrome check:
    return newS ==
        newS
            .split('')
            .reversed
            .join(''); // Compare original string with reversed string
  }
}
