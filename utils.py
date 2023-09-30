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
    
    return psn

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Asignación para asegurarse de que el número sea impar
        if sympy.isprime(num):
            return num

def pqs_generator():
    p = generate_prime(64)
    q = generate_prime(64)
    s = random.getrandbits(64)
    return p, q, s


# Key generation function using pseudo-random parameters
def generate_key(P, Q, seed):
    P0 = methods.scramble(P, seed)
    key = methods.generation(P0, Q)
    return key
    
def key_table_generator(p, q, s,key_number):
    keys = []
    for i in range(key_number):
        PO = methods.scramble(p, s)
        key = methods.generation(PO, q)
        keys.append(key)
        s = methods.mutation(s, q)
    return keys
