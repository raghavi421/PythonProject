 **Student Grade Calculator**
**title:** student grade calculator

** Objective**
The main objective of this project is to create a Python program that takes marks for different subjects from the user,
calculates the total marks, average, and finally assigns a grade based on the average score.
This project helps to understand how to use loops, conditional statements, and user input in Python.
 **Tools and Technologies Used**
Programming Language: Python 3
Platform: VS Code / Any Python IDE
Concepts Used:Variables,Loops,Conditional Statements (if-elif-else),User Input (input() function)
** Step-by-Step Procedure**
**Step 1:** Create a new Python file
Open Visual Studio Code (VS Code) → click File → New File → save it as
student_grade_calculator.py
**Step 2:** Write the following Python code

# Student Grade Calculator
# Step 1: Ask the user for number of subjects
num_subjects = int(input("Enter number of subjects: "))
# Step 2: Initialize total marks
total = 0
# Step 3: Loop to input marks for each subject
for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks
# Step 4: Calculate average
average = total / num_subjects
# Step 5: Determine grade based on average
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"
# Step 6: Display the result
print("\n------ Student Result ------")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
**Step 3:** Run the Program
To run the code, open the terminal in VS Code and type command.

**Sample Output**
Enter number of subjects: 3
Enter marks for subject 1: 85
Enter marks for subject 2: 78
Enter marks for subject 3: 92

------ Student Result ------
Total Marks: 255.0
Average Marks: 85.00
Grade: A
** Explanation**
The program asks the user for the number of subjects.
It then takes marks for each subject using a loop.
The total marks are calculated by adding all subject marks.
The average is obtained by dividing the total by the number of subjects.
Based on the average marks, a grade is assigned using if-elif-else conditions.
Finally, the program displays the total marks, average, and grade.
 **Conclusion**
This project demonstrates the use of basic Python concepts such as variables, loops, conditionals, and user input handling.
It is a simple yet effective program that helps beginners understand how to build logic and interact with users through Python code.


