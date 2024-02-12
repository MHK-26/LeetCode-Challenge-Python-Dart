class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initialization:
        rightSum = [1] * len(nums)  # Create an array the same size as 'nums' to store products from the right 
        leftSum = [1] * len(nums)   # Create an array the same size as 'nums' to store products from the left
        ans = [1] * len(nums)       # Create the result array, initialized with 1s 

        # Calculate prefix products:
        for i in range(1, len(nums)):  # Start from the second element 
            rightSum[i] = rightSum[i - 1] * nums[i - 1]  #  The product to the right of the current element is the product to the right of the previous element, multiplied by the previous element

        # Calculate suffix products:
        for i in range(len(nums) - 2, -1, -1):  # Start from the second to last element, going backwards
            leftSum[i] = leftSum[i + 1] * nums[i + 1]  # The product to the left of the current element is the product to the left of the next element, multiplied by the next element

        # Calculate final result:
        for i in range(len(nums)): 
            ans[i] = rightSum[i] * leftSum[i]  # For each element, multiply the corresponding prefix and suffix product 

        return ans
