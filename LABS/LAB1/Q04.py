InputList = []
numbers = int(input("Enter the number of digits: "))

for i in range(numbers):
    numbers = int(input("Enter the number: "))
    InputList.append(numbers)

print(InputList)

sum = 0

for items in InputList:
    sum = sum + items

print("The sum of the following numbers in the list is: " + str(sum))
