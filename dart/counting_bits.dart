class Solution {
  List<int> countBits(int n) {
    // Initialize a map to store the count of bits for each number
    Map<int, int> ans = {0: 0}; // Base case: 0 has 0 bits set

    // Iterate through numbers from 1 to n
    for (int i = 1; i <= n; i++) {
      // Note: The binary representation of any number can be obtained by
      // flooring the number resulting from dividing it by 2 and then shifting it to the left
      // (If the number is odd, an additional bit is added)

      // For even numbers, the count of bits is the same as for i/2
      if (i % 2 == 0) {
        ans[i] = ans[i ~/ 2]!;
      } else {
        // For odd numbers, add 1 to the count of bits for i/2
        ans[i] = ans[i ~/ 2]! + 1;
      }
    }

    // Convert map values to list and return
    return ans.values.toList();
  }
}
