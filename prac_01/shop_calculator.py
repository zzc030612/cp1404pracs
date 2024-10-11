item_price = 0
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    discounted_price = total_price * 0.90
else:
    discounted_price = total_price
print(f"Total price of {number_of_items} items is ${discounted_price:.2f}")
