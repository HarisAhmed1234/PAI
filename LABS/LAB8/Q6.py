import numpy as np

mat_a = np.random.randint(1, 10, size=(5, 3))  # 5x3 matrix
mat_b = np.random.randint(1, 10, size=(3, 2))  # 3x2 matrix

mat_result = np.dot(mat_a, mat_b)  # Multiply matrices

print("5x3 Matrix:\n", mat_a)
print("\n3x2 Matrix:\n", mat_b)
print("\nResult of multiplication (5x2 Matrix):\n", mat_result)
