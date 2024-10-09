import numpy as np

random_choices = [2, 5, 9, 10]
matrix_a = np.random.choice(random_choices, size=(4, 4))
identity_matrix = np.eye(4)
result_matrix = matrix_a @ identity_matrix
odd_numbers = np.arange(1, 32, 2)
odd_matrix = odd_numbers.reshape(4, 4)
final_matrix = result_matrix + odd_matrix

print("4x4 Matrix with Random Numbers (2, 5, 9, 10):")
print(matrix_a)
print("\nIdentity Matrix:")
print(identity_matrix)
print("\nResulting Matrix After Multiplication with Identity Matrix:")
print(result_matrix)
print("\n4x4 Matrix with Odd Numbers:")
print(odd_matrix)
print("\nFinal Matrix After Addition:")
print(final_matrix)
