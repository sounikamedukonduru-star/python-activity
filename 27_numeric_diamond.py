n = int(input("Enter diamond size: "))

if n <= 0:
    print("Invalid dimension")
else:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(i, end="")
        if i > 1:
            print(" " * (2 * i - 3), end="")
            print(i)
        else:
            print()

    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        print(i, end="")
        if i > 1:
            print(" " * (2 * i - 3), end="")
            print(i)
        else:
            print()
