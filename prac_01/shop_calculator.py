total = 0
numberItems = int(input("Number of items:"))
while numberItems < 0:
    print("Invalid")
    number = int(input("Number of items:"))
for i in range(numberItems):
    price = float(input("Price of item:"))
    total = total + price

if total > 100:
    discount = total * 0.10
    total = total - discount

print("Total price for ", numberItems, " items is $", total)