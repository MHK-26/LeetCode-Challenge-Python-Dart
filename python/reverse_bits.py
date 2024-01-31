class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0
        
        # Iterate through each bit (32 bits in a 32-bit integer)
        for i in range(0, 32):
            # Extract the i-th bit from the original number using right shift and bitwise AND
            m = (n >> i) & 1
            
            # Calculate the contribution of the current bit to the reversed number
            contribution = m * (2**(31 - i))
            
            # Accumulate the contribution to the reversed number
            number = number + contribution
         
        return number
