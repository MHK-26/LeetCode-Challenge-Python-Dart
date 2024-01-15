class Solution {
  // Function to find the indices of two numbers in a list that add up to a target
  List<int> twoSum(List<int> nums, int target) {
    final Map<int, int> hashMap =
        {}; // Create an empty HashMap for efficient lookups

    for (int i = 0; i < nums.length; i++) {
      int diff = target -
          nums[i]; // Calculate the complement needed to reach the target

      if (hashMap.containsKey(diff)) {
        // Check if the complement exists in the HashMap
        return [
          hashMap[diff]!,
          i
        ]; // If found, return the indices of the two numbers
      } else {
        hashMap[nums[i]] =
            i; // Store the current number and its index in the HashMap for future lookups
      }
    }

    return [0, 0]; // Return a default placeholder if no solution is found
  }
}
