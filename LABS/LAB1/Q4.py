inputlist=[]
numbers=int(input("enter the number of digits: "))
for i in range(numbers):
    numbers=int(input("enter the number: "))
    inputlist.append(numbers)
print(inputlist)
sum = 0

for i in inputlist:
    sum = sum + i

print(sum)
