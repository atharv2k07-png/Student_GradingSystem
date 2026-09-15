print("STUDENT GRADING SYSTEM")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))
social = float(input("Enter Social Science marks: "))

total = maths + science + english + computer + social
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print()
print("----------------------------")
print("     STUDENT RESULT")
print("----------------------------")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("----------------------------")

if grade == "F":
    print("Result: FAIL")
else:
    print("Result: PASS")

print("----------------------------")
print("Thank you!")