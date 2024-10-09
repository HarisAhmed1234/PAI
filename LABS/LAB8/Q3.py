import numpy as np

even_numbers = np.arange(2, 20, 2)
even_numbers_reshaped=even_numbers.reshape(3, 3)
multiplied_matrix = even_numbers_reshaped * 4
identity_matrix = np.eye(3)

result_matrix = multiplied_matrix @ identity_matrix
print("3x3 Matrix of Even Numbers: ")
print(even_numbers)
print("3x3 matrix reshaped: ")
print(even_numbers_reshaped)
print("Matrix Multiplied by 4: ")
print(multiplied_matrix)
print("Multiplied matrix multiply by identity matrix: ")
print(result_matrix)
