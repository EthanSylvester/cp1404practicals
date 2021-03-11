items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items.")
    items = int(input("Please enter a valid number of items: "))
price = 0
for n in range(0, items):
    value = float(input("Price of item: $"))
    price = price + value
if price > 100:
    price = price * 0.9
print("Total price for {} items is ${:.2f}".format(items, price))
