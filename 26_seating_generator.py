rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

reserved = [(1, 2), (2, 3)]

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if (i, j) in reserved:
            print("RES", end="\\t")
        elif (i + j) % 2 == 0:
            print("A" + str(i) + str(j), end="\\t")
        else:
            print("B" + str(i) + str(j), end="\\t")
    print()
