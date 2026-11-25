emails = ["abc@gmail.com", "student@college.in", "wrongemail"]

for email in emails:
    if "@" in email and "." in email:
        if email.index("@") < email.rindex("."):
            print(email, "Valid Email")
        else:
            print(email, "Invalid Email")
    else:
        print(email, "Invalid Email")

ids = ["NIAT123", "ABC456", "12@ABC"]

for x in ids:
    if x.isalnum():
        print(x, "Valid ID")
    else:
        print(x, "Invalid ID")
