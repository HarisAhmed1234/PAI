import numpy as np

dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'i4')]

data = np.array([
    ('Haris', np.random.uniform(1.5, 2.0), 2),
    ('Huzaifa', np.random.uniform(1.5, 2.0), 1),
    ('Sabeeh', np.random.uniform(1.5, 2.0), 2),
    ('Ali', np.random.uniform(1.5, 2.0), 1),
    ('Muhammad', np.random.uniform(1.5, 2.0), 2)
], dtype=dtype)

sorted_data = np.sort(data, order=['class', 'height'])

print("Sorted Structured Array:")
print(sorted_data)
