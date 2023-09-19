import random
import sympy
import os

# Funciones de generación de llaves
def fs(x, y):
    return (x ^ y) ^ (x >> 1)

def fg(x, y):
    return (x & y) ^ (x << 1)

def fm(x, y):
    return (x | y) ^ (y >> 1)

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if sympy.isprime(num):
            return num

def key_generator():
    p = generate_prime(64)
    q = generate_prime(64)
    s = random.getrandbits(64)
    return p, q, s

def key_table_generator(key_number, p, q, s):
    keys = []
    psn = 0  
    for i in range(key_number):
        PO = fs(p, s)
        key = fg(PO, q)
        keys.append(key)
        s = fm(s, q)
        psn = (psn + 1) % 16
    return keys

# funciones de encriptación
def fk1(x, key):
    return fs(x, key)

def fk2(x, key):
    return fg(x, key)

def fk3(x, key):
    return fm(x, key)

def fk4(x, key):
    return fs(x, key)

# Funciones de cifrado y descifrado
def format_message(id, type, payload, psn, encrypted_message):
    return f"ID: {id}\nTipo: {type}\nCarga Útil: {hex(payload)}\nPSN: {psn}\nMensaje Encriptado: {encrypted_message}"

def extract_message_components(message):
    lines = message.strip().split('\n')
    id = int(lines[0].split(': ')[1])
    type = int(lines[1].split(': ')[1])
    payload = int(lines[2].split(': ')[1], 16)
    psn = int(lines[3].split(': ')[1])
    encrypted_message = int(lines[4].split(': ')[1])
    return id, type, payload, psn, encrypted_message

def cipher_message(message, key, psn):
    encrypted_message = message
    psn_bits = psn.bit_length()
    for i in range(psn_bits):
        bit = (psn >> i) & 1
        if bit == 0:
            encrypted_message = fk1(encrypted_message, key)
        elif bit == 1:
            encrypted_message = fk2(encrypted_message, key)
        elif bit == 2:
            encrypted_message = fk3(encrypted_message, key)
        elif bit == 3:
            encrypted_message = fk4(encrypted_message, key)
        else:
            raise ValueError("Valor de PSN no válido")
    return encrypted_message

def divide_message(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    parts = []
    while len(binary_message) % 4 != 0:
        binary_message = '0' + binary_message
    for i in range(0, len(binary_message), 4):
        parts.append(binary_message[i:i+4])
    return parts

def get_last_psn(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            last_psn = int(last_line.split(': ')[1])
            return last_psn
        else:
            return 0

# Suma un valor aleatorio al psn anterior y asegura que el resultado tenga la cantidad correcta de bits
def select_psn_for_message(previous_psn, bits):
    random_bits = random.getrandbits(bits)
    new_psn = (previous_psn + random_bits) & ((1 << bits) - 1)
    return new_psn

# Guardar el mensaje encriptado en un archivo
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)

if __name__ == "__main__":
    cipher_key, decipher_key, seed = key_generator()
    key_number = 5
    key_table = key_table_generator(key_number, cipher_key, decipher_key, seed)

    original_message = input("Ingrese el mensaje a cifrar (máximo 64 caracteres): ")

    original_message = original_message[:64]

    message_file = "mensaje_encriptado.txt"

    message_parts = divide_message(original_message)

    last_psn = get_last_psn(message_file) if os.path.isfile(message_file) else 0

    # Seleccionar el PSN para el nuevo mensaje
    psn = select_psn_for_message(last_psn, 4)  

    # Asignar un ID aleatorio para el nuevo mensaje
    id = random.randint(0, 0x3F)  # 6 bits

    # Cifrar cada parte y construir el mensaje cifrado
    encrypted_message = 0
    for part in message_parts:
        encrypted_part = cipher_message(int(part, 2), key_table[0], psn)
        encrypted_message = (encrypted_message << 4) | encrypted_part

    formatted_message = format_message(id, 0, int(original_message.encode().hex(), 16), psn, encrypted_message)

    # Guardar el mensaje encriptado en un archivo 
    save_message(message_file, formatted_message)

    print("Mensaje encriptado guardado en mensaje_encriptado.txt")

    # Guardar la tabla de llaves en un archivo
    with open("llaves.txt", "w") as file:
        for i, key in enumerate(key_table, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves guardada en llaves.txt")