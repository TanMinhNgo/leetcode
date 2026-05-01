def maxProfit(self, prices: list[int], fee: int) -> int:
    bought = -prices[0]
    sold = 0

    for i in range(1, len(prices)):
        bought = max(bought, sold - prices[i])
        sold = max(sold, bought + prices[i] - fee)

    return sold