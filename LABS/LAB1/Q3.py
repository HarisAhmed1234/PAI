inputlist=[]
numbers=int(input("enter the number of digits: "))
for i in range(numbers):
    numbers=int(input("enter the number: "))
    inputlist.append(numbers)
print(inputlist)

count = 0

for i in inputlist:
    if(i % 2 == 0):
        count = count + 1
        
print(count)
