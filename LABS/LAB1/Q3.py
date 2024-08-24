Inputlist = []
numbers = int(input("enter the number of digits: "))
for i in range(numbers):
    numbers = int(input("enter the number: "))
    Inputlist.append(numbers)
print(Inputlist)

count = 0

for i in Inputlist:
    if (i % 2 == 0):
        count = count + 1

print("The even numbers in this list are: " + str(count))
