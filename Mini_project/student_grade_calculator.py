def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)


average = calculate_average(marks)
grade = calculate_grade(average)


print("\n--- Student Result ---")
print("Student:", name)
print("Marks:", marks)
print("Average:", round(average, 2))
print("Grade:", grade)