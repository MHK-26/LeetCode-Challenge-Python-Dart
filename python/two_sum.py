class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hashMap = {}  # Create a dictionary for efficient lookups

            for i in range(len(nums)):
                diff = target - nums[i]  # Calculate the complement needed to reach the target

                if diff in hashMap:  # Check if the complement has been seen before
                    return [hashMap[diff], i]  # If found, return the indices of the two numbers

                # Store the current number and its index in the dictionary for future lookups
                hashMap[nums[i]] = i

            return []  # Return an empty list if no solution is found