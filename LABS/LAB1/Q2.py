n1 = float(input("Enter first number: "))
n2 = float(input("Enter seconnd number: "))
n3 = float(input("Enter third number: "))
operator = input("Enter the operation you want to perform: ")
result = 0

if(operator == "+"):
    result = n1 + n2 + n3
elif(operator == "-"):
    result = n1 - n2
elif(operator == "*"):
    result = n1 * n2 * n3
elif(operator == "/"):
    result= n1 / n2
else:
    print("Invalid Operator")
