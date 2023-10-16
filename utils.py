import hashlib
import random
import sympy
from functions import methods

# FUNCION DE SELECCION DE PSN

def select_psn(message):
   # Convierte a hash el mensaje para generar un digest
    message_digest = hashlib.sha256(message.encode()).digest()
    
    # Toma el primer byte del digest como PSN
    psn = int.from_bytes(message_digest[:1], byteorder='big')
    
    # rango de 0 a 2
    psn %= 3
    
    return psn

# Genera un número primo con 'bits' de longitud, es utilizado para la generacion de P y Q
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Asignación para asegurarse de que el número sea impar
        if sympy.isprime(num):
            return num

# Genera valores P, Q y S para claves criptográficas        
def pqs_generator():
    p = generate_prime(64)
    q = generate_prime(64)
    s = random.getrandbits(64)
    return p, q, s

# Genera una clave criptográfica utilizando P, Q y un valor 'seed'
def generate_key(P, Q, seed):
    P0 = methods.scramble(P, seed)
    key = methods.generation(P0, Q)
    return key
    
# Funcion para generar la tabla de claves criptográficas    
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