# 5. Grade Calculator
# Function that returns a letter grade based on marks using if-elif-else.
def calculate_grade(marks):
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'Fail'

    print(f"\nMarks: {marks}, Grade: {grade}")
    return grade
Marks = int(input("Enter Marks: "))
calculate_grade(Marks)
