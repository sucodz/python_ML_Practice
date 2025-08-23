import numpy as np  

# Generate 5000 random height values using a normal distribution
# np.random.normal(mean, standard_deviation, number_of_samples)
# mean = 1.75 meters, std = 0.20, and we want 5000 people
# np.round(..., 2) rounds each value to 2 decimal places
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

# Generate 5000 random weight values using a normal distribution
# mean = 60.32 kg, std = 15, with 5000 samples
# also rounded to 2 decimal places
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

# Combine the height and weight arrays into a 2D array (like a table)
# np.column_stack((array1, array2)) stacks them as columns side by side
# Result: 5000 rows × 2 columns → [[height, weight], [height, weight], ...]
np_city = np.column_stack((height, weight))

# Preview the first 5 rows to see the result
print(np_city[:5])
