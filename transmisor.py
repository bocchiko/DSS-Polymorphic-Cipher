import random

def key_generator():
    p = random.getrandbits(64)
    q = random.getrandbits(64)
    s = random.getrandbits(64)
    return p, q, s

def key_table_generator(key_number, p, q, s):
    keys = []
    for i in range(key_number):
        PO = scramble(p, s)
        key = generation(PO, q)
        keys.append(key)
        s = mutation(s, q)
    return keys

def scramble(x, y):
    return (x ^ y) ^ (x >> 1)

def generation(x, y):
    return (x & y) ^ (x << 1)

def mutation(x, y):
    return (x | y) ^ (y >> 1)

def cipher_message(message, key):
    encrypted = []
    for char in message:
        char_code = ord(char)
        encrypted_char_code = char_code ^ key
        encrypted.append(encrypted_char_code)
    return encrypted

def descipher_message(encrypted_message, key):
    decrypted = ""
    for char_code in encrypted_message:
        char_code = char_code ^ key
        decrypted_char = chr(char_code)
        decrypted += decrypted_char
    return decrypted

if __name__ == "__main__":
    cipher_key, descipher_key, seed = key_generator()
    key_number = 5
    key_table = key_table_generator(key_number, cipher_key, descipher_key, seed)
    original_message = input("Ingrese un mensaje a cifrar: ")
    
    with open("llaves.txt", "w") as file:
        for i, key in enumerate(key_table, 1):
            file.write(f"Numero de llave {i}: {key}\n")
    
    print("Tabla de llaves guardada en llaves.txt")

    for key in key_table:
        encrypted_message = cipher_message(original_message, key)
        decrypted_message = descipher_message(encrypted_message, key)
        print("Clave: ", key)
        print("Mensaje Cifrado: ", encrypted_message)
        print("Mensaje Descifrado: ", decrypted_message)

