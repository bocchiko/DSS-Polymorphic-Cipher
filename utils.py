import hashlib
import random
import sympy
from functions import methods
# PSN selection function (you need to implement this based on your message structure)
def select_psn(message):
   # Hash the message to generate a digest
    message_digest = hashlib.sha256(message.encode()).digest()
    
    # Take the first byte of the digest as the PSN
    psn = int.from_bytes(message_digest[:1], byteorder='big')
    
    # Ensure the PSN is in the valid range (0-15)
    psn %= 16
    
    return random.randint(0, 3)

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Asignación para asegurarse de que el número sea impar
        if sympy.isprime(num):
            return num

def generate_random_prime():
    # Define the number of bits for the prime
    num_bits = 16

    # Generate a random integer with the specified number of bits
    random_integer = random.getrandbits(num_bits)

    # Ensure the random integer is odd (to increase the chances of getting a prime)
    if random_integer % 2 == 0:
        random_integer += 1

    # Find the next prime number starting from the random integer
    random_prime = sympy.nextprime(random_integer)

    print(f"Random 64-bit prime number: {random_prime}")

def pqs_generator():
    p = generate_prime(64) #sympy.randprime(1, 100) 
    q = generate_prime(64) #sympy.randprime(1, 100)
    s = random.getrandbits(64) #random.randint(1, 100)
    """  p = sympy.randprime(1, 100) 
    q = sympy.randprime(1, 100)
    s = random.randint(1, 100) """
    return p, q, s


# Key generation function using pseudo-random parameters
def generate_key(P, Q, seed):
    P0 = methods.scramble(P, seed)
    key = methods.generation(P0, Q)
    return key
    
def key_table_generator(p, q, s,key_number):
    keys = []
    for _ in range(key_number):
        PO = methods.scramble(p, s)
        key = methods.generation(PO, q)
        keys.append(key)
        s = methods.mutation(s, q)
    return keys
