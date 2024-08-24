MarksDictionary = {}

MarksDictionary["Physics"] = int(input("Enter marks for Physics: "))
MarksDictionary["Chemistry"] = int(input("Enter marks for Chemistry: "))
MarksDictionary["Maths"] = int(input("Enter marks for Maths: "))

total_marks = 0
highest_marks = 0
highest_marks_subject = ""

for subject, marks in MarksDictionary.items():
    total_marks += marks
    if marks > highest_marks:
        highest_marks = marks
        highest_marks_subject = subject

average = total_marks / len(MarksDictionary)

print("The average of the marks is: " + str(round(average,1)))
print("The subject in which she got the highest marks is: " + highest_marks_subject)
