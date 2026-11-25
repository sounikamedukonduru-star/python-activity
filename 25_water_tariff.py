n = int(input("Enter number of households: "))

for i in range(n):
    units = int(input("Enter water units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = bill + 50

    if units > 300:
        bill = bill + 100

    print("Water Bill:", bill)
