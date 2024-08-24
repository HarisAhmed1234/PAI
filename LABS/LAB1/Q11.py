MarksDictionary = {}

MarksDictionary["Physics"] = int(input("Enter marks for Physics: "))
MarksDictionary["Chemistry"] = int(input("Enter marks for Chemistry: "))
MarksDictionary["Maths"] = int(input("Enter marks for Maths: "))

total_marks = 0
for marks in MarksDictionary.values():
    total_marks += marks

average = total_marks / len(MarksDictionary)

percentage = (total_marks / (len(MarksDictionary) * 100)) * 100

print("The average of the marks is: " + str(round(average, 1)))
print("The percentage of the marks is: " + str(round(percentage, 1)) + "%")
