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


# Key generation function using pseudo-random parameters
def generate_key(P, Q, seed):
    P0 = methods.scramble(P, seed)
    key = methods.generation(P0, Q)
    return key

# Funciones que crea la tabla de llaves    
def key_table_generator(p, q, s,key_number):
    keys = []
    for _ in range(key_number):
        PO = methods.scramble(p, s)
        key = methods.generation(PO, q)
        keys.append(key)
        s = methods.mutation(s, q)
    return keys


# Funcion para formatear el mensaje con id, tipo, payload y psn
def format_message(id, type, payload, psn):
    return f"{id}\n{type}\n{payload}\n{psn}"
    
# Guardar el mensaje encriptado en un archivo
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)