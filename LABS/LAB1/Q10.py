size = int(input("Enter the size of the list: "))
InputList = []

for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    InputList.append(num)

largest = max(InputList)
print("The largest number in the list is:", largest)
