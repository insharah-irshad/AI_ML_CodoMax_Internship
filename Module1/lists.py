subjects = ["Python", "AI", "Math", "Computer Networks"]

print(subjects)

subjects = ["Python", "AI", "Math", "Computer Networks"]

print(subjects[0])
print(subjects[1])
print(subjects[2])

subjects = ["Python", "AI", "Math"]

subjects.append("English")

print(subjects)

subjects.remove("Math")

print(subjects)

subjects = ["Python", "AI", "Math", "Computer Networks"]

for subject in subjects:
    print("Subject:", subject)


marks = [78, 85, 91, 67, 88]

print("Total:", sum(marks))
print("Number of subjects:", len(marks))
print("Average:", sum(marks) / len(marks))
