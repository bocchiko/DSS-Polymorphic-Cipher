import hashlib
import random
import sympy
from functions import methods

# Funcion de Seleccion de PSN
def select_psn(message):
   # Convierte a hash el mensaje para generar un digest
    message_digest = hashlib.sha256(message.encode()).digest()
    
    # Toma el primer byte del digest como PSN
    psn = int.from_bytes(message_digest[:1], byteorder='big')
    
    # rango de 0 a 2
    psn %= 3
    
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

# Funciones que crea la tabla de llaves    
def key_table_generator(p, q, s,key_number):
    keys = []
    for i in range(key_number):
        PO = methods.scramble2(p, s)
        key = methods.generation2(PO, q)
        keys.append(key)
        s = methods.mutation2(s, q)
    return keys
