
products = ["Хлеб", "Молоко", "Яблоки"]


prices = (30, 85, 120)


total = sum(prices)


print("Чек:")
for product, price in zip(products, prices):
    print(f"{product} - {price} руб.")

print(f"Итого: {total} руб.")