class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a dictionary to store the count of bits for each number
        ans = {0: 0}  # Base case: 0 has 0 bits set
        for i in range(1, n + 1):  # Loop through numbers from 1 to n
            if i % 2 == 0:
                # If the number is even, the count of bits is the same as for i/2
                ans[i] = ans[i // 2]
            else:
                # If the number is odd, add 1 to the count of bits for i/2
                ans[i] = ans[i // 2] + 1 
        return list(ans.values())  # Convert dict values to list and return



            # Note: The binary representation of any number can be obtained by 
            # flooring the number resulting from dividing it by 2 and then shifting it to the left
            # (If the number is odd, an additional bit is added (1))