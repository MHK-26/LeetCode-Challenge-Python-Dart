class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Counts the number of 1 bits (Hamming weight) in the binary representation of an integer.
        """

        count = 0  # Initialize counter for 1 bits

        while n > 0:          
            count += n % 2  # Check the rightmost bit:# Increment count if it's a 1

            # Shift n one bit to the right to examine the next bit:
            n = n >> 1

        return count  # Return the final count of 1 bits
