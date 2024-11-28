import numpy as np
rand_array = np.random.rand(1000)  # Random array with 1000 elements

mean_val = np.mean(rand_array)  # Calculate mean
var_val = np.var(rand_array)  # Calculate variance
std_val = np.std(rand_array)  # Calculate standard deviation

# Save the results to a text file
with open("results.txt", "w") as output_file:
    output_file.write(f"Average: {mean_val}\nVariance: {var_val}\nStandard Deviation: {std_val}")
