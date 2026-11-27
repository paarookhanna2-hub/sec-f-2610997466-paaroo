
# STEP 1: Import NumPy
import numpy as np

# STEP 2: Display heading
print("=" * 50)
print("SCIENTIFIC DATA PROCESSING TOOL")
print("=" * 50)

# STEP 3: Ask number of readings
n = int(input("How many readings do you want to enter? "))

# STEP 4: Create empty list
readings_list = []

# STEP 5: Take readings from user
for i in range(n):
    value = float(input(f"Enter reading {i+1}: "))
    readings_list.append(value)

# STEP 6: Convert list into NumPy array
readings = np.array(readings_list)

# STEP 7: Display original array
print("\n--- Array Details ---")
print("Original Readings:", readings)

# STEP 8: Display array properties
print("Dimensions (ndim):", readings.ndim)
print("Shape:", readings.shape)
print("Total Items (size):", readings.size)
print("Data Type (dtype):", readings.dtype)

# STEP 9: Create zero array
baseline = np.zeros(n)
print("Baseline (Zeros):", baseline)

# STEP 10: Take adjustment value
print("\n--- Adjust Readings ---")
offset = float(input("Enter adjustment value to add: "))

# STEP 11: Take multiplier
multiplier = float(input("Enter multiplier value to scale: "))

# STEP 12: Add offset
adjusted_addition = readings + offset

# STEP 13: Multiply readings
adjusted_multiplication = readings * multiplier

# Display final results
print("\n--- Adjusted Arrays ---")
print("After adding", offset, ":", adjusted_addition)
print("After multiplying by", multiplier, ":", adjusted_multiplication)

print("=" * 50)
