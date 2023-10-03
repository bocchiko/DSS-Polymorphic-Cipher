def scramble(x, y):
    return (x ^ y) ^ (x >> 1)

def generation(x, y):
    return (x & y) ^ (x << 1)

def mutation(x, y):
    return (x | y) ^ (y >> 1)

def fs_inverse(x, y):
    return ((x >> 1) ^ y) ^ x

def fg_inverse(x, y):
    return ((x << 1) ^ y) ^ (x & y)

def fm_inverse(x, y):
    return ((y >> 1) ^ x) ^ (x | y)

# Reversible functions 
def scramble(x, y):
    return (x ^ y) ^ (x >> 1)

def generation(x, y):
    return (x & y) ^ (x << 1)

def mutation(x, y):
    return (x | y) ^ (y >> 1)

def inverse_scramble(char_code, key):
    # Reverse the scramble operation
    return (char_code ^ key) ^ (char_code >> 1)

# Inverse of the generation function
def inverse_generation(char_code, key):
    # Reverse the generation operation
    return (char_code ^ key) ^ (char_code << 1)

# Inverse of the mutation function
def inverse_mutation(char_code, key):
    # Reverse the mutation operation
    return (char_code ^ (char_code | key)) ^ (key >> 1)

# Function to apply reversible functions with PSN
def apply_reversible_functions(char_code, key, psn):
    # Convert char_code, key, and psn to 32-bit integers
    char_code &= 0xFFFFFFFF
    key &= 0xFFFFFFFF
    psn &= 0xF
    
    # Apply the reversible functions based on PSN
    if psn == 0:
        return inverse_scramble(char_code, key)
    elif psn == 1:
        return inverse_generation(char_code, key)
    elif psn == 2:
        return inverse_mutation(char_code, key)
    # Add more cases for different PSN values if needed
  
    # Default case: no transformation (identity)
    return char_code