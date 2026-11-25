invoice = "P101,2,500;P102,3,200;P103,1,100"

items = invoice.split(";")
total = 0

for item in items:
    data = item.split(",")

    if len(data) == 3:
        code = data[0]
        quantity = int(data[1])
        price = int(data[2])

        amount = quantity * price
        total = total + amount

        print("Product:", code)
        print("Quantity:", quantity)
        print("Amount:", amount)
    else:
        print("Invalid Record")

print("Total Invoice:", total)
