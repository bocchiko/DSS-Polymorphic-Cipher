def reverse_operation(result, x):
    # Calculate y using the inverse of x >> 1 operation
    y = (result ^ (x >> 1)) ^ x
    return y

# Example usage
original_x = 10
original_y = 5

# Calculate the result using the original operation
original_result = (original_x ^ original_y) ^ (original_x >> 1)

# Attempt to reverse the operation to find original y
reversed_y = reverse_operation(original_result, original_x)

print(f"Original x: {original_x}")
print(f"Original y: {original_y}")
print(f"Calculated result: {original_result}")
print(f"Reversed y: {reversed_y}")