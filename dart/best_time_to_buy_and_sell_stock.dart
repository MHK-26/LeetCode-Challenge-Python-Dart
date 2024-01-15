class Solution {
  // Function to calculate the maximum profit that can be made by buying and selling a stock once
  int maxProfit(List<int> prices) {
    // Initialize pointers for tracking buy and sell positions
    int l = 0; // Left pointer (buy)
    int r = 1; // Right pointer (sell)

    // Initialize the maximum profit to zero
    int profit = 0;

    // Iterate through the prices using two pointers
    while (r < prices.length) {
      // If the current price is lower than the previous price,
      // update the buy pointer to the current position
      if (prices[l] > prices[r]) {
        l = r;
        r = r + 1;
      } else {
        // Calculate the potential profit
        final currentProfit = prices[r] - prices[l];

        // Update the maximum profit if the potential profit is higher
        profit = currentProfit > profit ? currentProfit : profit;

        // Move the sell pointer to the next day
        r = r + 1;
      }
    }

    // Return the maximum achievable profit
    return profit;
  }
}
