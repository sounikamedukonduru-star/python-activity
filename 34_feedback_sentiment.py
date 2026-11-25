positive = ["good", "excellent", "helpful", "nice"]
negative = ["bad", "poor", "worst", "difficult"]

feedback = [
    "The teacher is good and helpful",
    "The class is bad",
    "Excellent teaching"
]

for sentence in feedback:
    words = sentence.lower().split()
    pos = 0
    neg = 0

    for word in words:
        if word in positive:
            pos += 1
        if word in negative:
            neg += 1

    score = pos - neg

    print("Feedback:", sentence)
    print("Positive:", pos)
    print("Negative:", neg)
    print("Score:", score)

    if score > 0:
        print("Positive Feedback")
    elif score < 0:
        print("Negative Feedback")
    else:
        print("Neutral Feedback")
