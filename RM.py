# Regular Message (RM)
# Este programa es para encriptar y desencriptar mensajes. Este programa lee el txt con la tabla de llaves para encriptar y desencriptar un mensaje
# El resultado de encriptacion y desencriptacion se muestra en la consola 

from functions import methods
import utils

# Funcion de Encriptacion
def encrypt(message, keys, psn):
    encrypted_message = []
    key_index = 0
    
    for char in message:
        char_code = ord(char)
        key = keys[key_index]
        encrypted_char_code = methods.apply_reversible_functions(char_code, key, psn)
        encrypted_message.append(encrypted_char_code)
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0
    
    return encrypted_message

# Funcion de Desencriptacion
def decrypt(encrypted_message, keys, psn):
    decrypted_message = []
    key_index = 0
    
    for char_code in encrypted_message:
        key = keys[key_index]
        decrypted_char_code = methods.apply_reversible_functions(char_code, key, psn)
        
        decrypted_char_code %= 0x110000
        decrypted_message.append(chr(decrypted_char_code))
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0
    
    return ''.join(decrypted_message)

def format_message(id, type, payload, psn):
    return f"{id}\n{type}\n{payload}\n{psn}"

# Guardar el mensaje encriptado en un archivo
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)

if __name__ == "__main__":

    keys = []
    with open("results/llaves.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(": ")
            if len(parts) == 2:
                key = int(parts[1])
                keys.append(key)
    
    message = input("Ingrese el mensaje a cifrar (máximo 64 caracteres): ")
    psn = utils.select_psn(message)  # Selecciona PSN en base al mensaje
    
    encrypted_message = encrypt(message, keys, psn)
    decrypted_message = decrypt(encrypted_message, keys, psn)

    ft_message = format_message('{:06d}'.format(1), '{:04d}'.format(1), encrypted_message , psn)
    save_message('results/RM_Server_result.txt', ft_message)
    
    
    print("Client Encrypted Message:", encrypted_message)
    print("Decrypted Server Message:", decrypted_message)