# Canteen menu prices (rupiah)
prices = [15000, 22000, 8000, 30000]
# Make a discounted copy: 2000 off every item
sale_prices = prices
price = prices.copy()
for i in range(len(sale_prices)):
    sale_prices[i] = sale_prices[i] - 2000
# Raise every normal price by 1000
for b in range(len(price)):
    price[b] = price[b] + 1000
print("Normal:", price)
print("Sale:", sale_prices)


