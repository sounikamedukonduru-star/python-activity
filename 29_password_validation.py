passwords = ["Hello123@", "abc", "Password", "Test@123"]

for p in passwords:
    if len(p) < 8:
        print(p, "Invalid: Minimum 8 characters")
    elif not any(c.isupper() for c in p):
        print(p, "Invalid: No uppercase letter")
    elif not any(c.islower() for c in p):
        print(p, "Invalid: No lowercase letter")
    elif not any(c.isdigit() for c in p):
        print(p, "Invalid: No digit")
    elif not any(not c.isalnum() for c in p):
        print(p, "Invalid: No special character")
    elif any(p[i] == p[i + 1] for i in range(len(p) - 1)):
        print(p, "Invalid: Repeated characters")
    else:
        print(p, "Valid Password")
