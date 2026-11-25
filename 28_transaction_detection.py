ids = [101, 102, 103, 101, 104, 102]
amounts = [500, 2000, 15000, 500, 300, 12000]

duplicates = []
suspicious = []

for i in range(len(ids)):
    if ids[i] in ids[:i]:
        duplicates.append(ids[i])

    if amounts[i] > 10000:
        suspicious.append(ids[i])

print("Duplicate Transactions:", duplicates)
print("Suspicious Transactions:", suspicious)
