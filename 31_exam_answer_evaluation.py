key = ["A", "B", "C", "D", "A"]
answers = ["A", "B", "D", "", "A"]

correct = 0
wrong = 0
unanswered = 0

for i in range(len(key)):
    if answers[i] == "":
        unanswered += 1
    elif answers[i] == key[i]:
        correct += 1
    else:
        wrong += 1

score = correct * 2 - wrong * 0.5

print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Unanswered:", unanswered)
print("Final Score:", score)
