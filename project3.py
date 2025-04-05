score = int(input("Enter your score to know your grade: "))
if score > 90:
    print("Grade: A")
elif score <= 90 and score > 80:
    print("Grade: B")
elif score <= 80 and score >= 60:
    print("Grade: C")
else:
    print("Grade: F")