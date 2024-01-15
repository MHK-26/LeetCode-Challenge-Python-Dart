class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Initialize two pointers: left (buy) and right (sell)
        profit = 0  # Initialize the maximum profit to zero

        while r < len(prices):  # Iterate through the prices using two pointers
            if prices[l] > prices[r]:  # If the current price is lower than the previous price
                l = r  # Update the buy pointer to the current position
                r += 1  # Move the sell pointer to the next day
            else:
                potential_profit = prices[r] - prices[l]  # Calculate potential profit
                if potential_profit > profit:  # If potential profit is higher than current max profit
                    profit = potential_profit  # Update the maximum profit
                r += 1  # Move the sell pointer to the next day

        return profit  # Return the maximum achievable profit