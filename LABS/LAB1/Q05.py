InputList = []
numbers = int(input("Enter the number of digits: "))

for i in range(numbers):
    num = int(input("Enter the number: "))
    InputList.append(num)

print("Original List:", InputList)

comparisonNumber = int(input("Enter the number to compare against: "))

InputList = [items for items in InputList if items >= comparisonNumber]

print("The list after removing elements less than " + str(comparisonNumber) + " is: " + str(InputList))
