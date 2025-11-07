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