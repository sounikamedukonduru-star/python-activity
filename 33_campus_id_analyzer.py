# Assumed ID format: YY-BR-XXXX
ids = ["24-CS-1001", "25-IT-1002", "23-EC-1003"]

for x in ids:
    parts = x.split("-")

    if (len(parts) == 3 and len(parts[0]) == 2
            and len(parts[1]) == 2 and len(parts[2]) == 4):
        year = parts[0]
        branch = parts[1]
        number = parts[2]

        if year.isdigit() and branch.isalpha() and number.isdigit():
            print("Valid ID:", x)
            print("Admission Year:", "20" + year)
            print("Branch:", branch)
            print("Student Number:", number)
        else:
            print("Invalid ID")
    else:
        print("Invalid ID")
