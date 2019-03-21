total_price = 0
number_of_items = int(input("Please enter the number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price
if total_price > 100:
    total_price = (total_price * 0.9)
print("The total price for {} items is ${:.2f}".format(number_of_items, total_price))