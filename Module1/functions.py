def calculate_average(marks):
    return sum(marks) / len(marks)


def check_result(average):
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


marks = [85, 78, 92, 88, 76]

average = calculate_average(marks)
grade = check_result(average)

print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)