class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ""
        for c in s:
            if c.isalnum():
                test += c.lower()
        return test == test[::-1]
