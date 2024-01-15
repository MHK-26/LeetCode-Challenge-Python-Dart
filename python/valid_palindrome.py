class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome (reads the same backward and forward).

        Args:
            s: The input string.

        Returns:
            True if the string is a palindrome, False otherwise.
        """

        test = ""  # Initialize an empty string to store alphanumeric characters

        # Preprocess the string:
        for c in s:
            if c.isalnum():  # Check if the character is alphanumeric
                test += c.lower()  # Add it to the test string in lowercase

        # Palindrome check:
        return test == test[::-1]  # Compare the test string with its reversed version

    #this code by doing your own  alphanum function
    # class Solution:
    # def isPalindrome(self, s: str) -> bool:
  
    #     l, r = 0, len(s) - 1
    #     while l < r:
    #         while l < r and not self.alphanum(s[l]):
    #             l += 1
    #         while l < r and not self.alphanum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

    # # Could write own alpha-numeric function
    # def alphanum(self, c):
    #     return (
    #         ord("A") <= ord(c) <= ord("Z")
    #         or ord("a") <= ord(c) <= ord("z")
    #         or ord("0") <= ord(c) <= ord("9")
    #     )

        