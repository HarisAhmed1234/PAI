def multiply_list():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    result = 1
    for num in numbers:
        result = result * num

    return result

print(f"The product of the list is: {multiply_list()}")
