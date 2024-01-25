class Solution {
  int climbStairs(int n) {
    // Base cases: If there is only one stair, there's one way to climb (1)
    // If there are two stairs, there are two ways to climb (1+1 or 2)
    if (n == 1) {
      return 1;
    }
    if (n == 2) {
      return 2;
    }

    // Map to store the number of ways to climb for each number of stairs
    Map<int, int> dp = {};
    dp[1] = 1; // There is 1 way to climb 1 stair
    dp[2] = 2; // There are 2 ways to climb 2 stairs (1+1 or 2)

    // Dynamic programming approach to calculate the number of ways to climb for each number of stairs
    for (int i = 3; i <= n; i++) {
      // The number of ways to climb 'i' stairs is the sum of the ways to climb 'i-2' and 'i-1' stairs
      dp[i] = dp[i - 2]! + dp[i - 1]!;
    }

    // The result is the number of ways to climb 'n' stairs
    return dp[n]!;
  }
}
