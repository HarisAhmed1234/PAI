def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of iss {factorial(user_input)}")
