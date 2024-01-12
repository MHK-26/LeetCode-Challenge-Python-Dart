class Solution {
  int maxProfit(List<int> prices) {
    int l = 0;
    int r = 1;
    int profit = 0;

    while (r < prices.length) {
      if (prices[l] > prices[r]) {
        l = r;
        r = r + 1;
      } else {
        final currentProfit = prices[r] - prices[l];
        profit = currentProfit > profit ? currentProfit : profit;
        r = r + 1;
      }
    }

    return profit;
  }
}
