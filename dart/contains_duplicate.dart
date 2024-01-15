class Solution {
  // Function to determine if a list of integers contains any duplicates
  bool containsDuplicate(List<int> nums) {
    // Create an empty set to efficiently track unique elements
    Set<int> seenNumbers = {};

    // Iterate through each number in the list
    for (int n in nums) {
      // If the number is already in the set, it's a duplicate
      if (seenNumbers.contains(n)) {
        return true; // Return immediately as a duplicate is found
      }

      // Otherwise, add the number to the set to mark it as seen
      seenNumbers.add(n);
    }

    // If the loop completes without finding duplicates, return false
    return false;
  }
}
