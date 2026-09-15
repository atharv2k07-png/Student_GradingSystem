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
Example Output
STUDENT GRADING SYSTEM

Enter student name: Atharv
Enter Maths marks: 92
Enter Science marks: 85
Enter English marks: 88
Enter Computer marks: 95
Enter Social Science marks: 80

----------------------------
     STUDENT RESULT
----------------------------
Name: Atharv
Total Marks: 440.0
Percentage: 88.0 %
Grade: A
----------------------------
Result: PASS
----------------------------
Thank you!
2. GitHub Description

Use:

A simple Python-based Student Grading System that calculates total marks, percentage, grade, and pass/fail result.

3. README.md

Create README.md in the same folder and paste:

# 🎓 Student Grading System

A simple and beginner-friendly **Student Grading System built using Python**.

The program takes marks for different subjects, calculates the total marks and percentage, and automatically assigns a grade and pass/fail result.

## 🚀 Features

- Enter student name
- Enter marks for 5 subjects
- Calculate total marks
- Calculate percentage
- Automatically assign grades
- Display pass/fail result
- Simple command-line interface

## 🛠️ Technologies Used

- Python 3
- VS Code

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Student-Grading-System.git
Open the project in VS Code.
Run the program:
python student_grading.py
📊 Grading System
Percentage	Grade
90 - 100	A+
80 - 89	A
70 - 79	B
60 - 69	C
50 - 59	D
Below 50	F
🎯 Purpose

This project was created as a Python mini project to practice programming fundamentals such as:

Variables
User input
Data types
Arithmetic operations
Conditional statements
Basic automation
👨‍💻 Author

Atharv Rastogi

B.Tech CSE – Artificial Intelligence & Data Engineering

⭐ If you found this project useful, consider giving it a star!


### Recommended GitHub repository name

**`Student-Grading-System`**

So your Unit 2 mini-project will look clean and professional on GitHub.
now give me description

GitHub description:

A simple Python-based Student Grading System that calculates total marks, percentage, grade, and pass/fail status based on student performance.

now a sexy readme

Absolutely 😎 Here’s a clean, modern, “sexy” GitHub README without making a beginner project look unnecessarily complicated.

Copy this into README.md:

# 🎓 Student Grading System

> 📊 A simple Python program that turns student marks into meaningful results.

---

## ✨ Overview

The **Student Grading System** is a beginner-friendly Python mini project that automates the process of calculating a student's total marks, percentage, grade, and final result.

Instead of manually calculating everything, just enter the marks and let Python do the work. ⚡

---

## 🚀 Features

- 👤 Student name input
- 📝 Marks input for 5 subjects
- ➕ Automatic total calculation
- 📈 Percentage calculation
- 🏆 Automatic grade assignment
- ✅ Pass / ❌ Fail status
- 💻 Simple command-line interface

---

## 🧠 How It Works

```text
Student Marks
      ↓
Calculate Total
      ↓
Calculate Percentage
      ↓
Assign Grade
      ↓
Display Result
📊 Grading Criteria
Percentage	Grade
90 – 100%	🟢 A+
80 – 89%	🟢 A
70 – 79%	🔵 B
60 – 69%	🟡 C
50 – 59%	🟠 D
Below 50%	🔴 F
💻 Example
STUDENT GRADING SYSTEM

Enter student name: Atharv

Enter Maths marks: 92
Enter Science marks: 85
Enter English marks: 88
Enter Computer marks: 95
Enter Social Science marks: 80

----------------------------
     STUDENT RESULT
----------------------------
Name: Atharv
Total Marks: 440.0
Percentage: 88.0 %
Grade: A
----------------------------
Result: PASS
----------------------------
Thank you!
🛠️ Tech Stack

Language: Python 🐍

Editor: Visual Studio Code 💻

📚 Concepts Used

This project helped practice fundamental Python concepts:

Variables
User Input
Data Types
Arithmetic Operations
Conditional Statements
Basic Automation
Formatted Output
▶️ Run Locally
1. Clone the repository
git clone https://github.com/your-username/Student-Grading-System.git
2. Open the project
cd Student-Grading-System
3. Run the program
python student_grading.py
🎯 Project Goal

The goal of this project is to understand how Python can be used to automate simple real-world tasks while strengthening programming fundamentals.

🔮 Future Improvements

Some features that could be added in future versions:

📋 Support for multiple students
💾 Save results to a file
📊 Generate student reports
🖥️ Add a graphical user interface
🗃️ Store student records
👨‍💻 Author
Atharv Rastogi

🎓 B.Tech CSE – Artificial Intelligence & Data Engineering

<div align="center">

⭐ If you found this project useful, consider giving it a star!

Made with 🐍 Python

</div> ```
