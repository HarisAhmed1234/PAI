import numpy as np

odd_array=np.arange(1,19,2)
two_dimensional_array=odd_array.reshape(3,3)

for row in  two_dimensional_array:
        print(row)
