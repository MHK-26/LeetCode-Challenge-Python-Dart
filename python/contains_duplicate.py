class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
 
        seen_numbers = set()  # Create an empty set to track unique elements

        for n in nums:
            if n in seen_numbers:  # Check if the number is already seen
                return True  # Duplicate found, return immediately
            seen_numbers.add(n)  # Add the number to the set if not seen

        return False  # No duplicates found
