# Regular Message (RM)
# Este programa es para encriptar y desencriptar mensajes. Este programa lee el txt con la tabla de llaves para encriptar y desencriptar un mensaje
# El resultado de encriptacion y desencriptacion se muestra en la consola 

from functions import methods
import utils

# Funcion de Encriptacion
def encrypt(message, keys):
    encrypted_message = []
    key_index = 0
    orderPsn = []
    
    for char in message:
        key = keys[key_index]
        psn = utils.select_psn(message)
        char_code = ord(char)
        if psn == 0:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk1(char_code, key)
            encrypted_message.append(encrypted_char_code )
        elif psn == 1:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk2(char_code, key)
            encrypted_message.append(encrypted_char_code )
        elif psn == 2:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk3(char_code, key)
            encrypted_message.append(encrypted_char_code )
        else:
            raise ValueError("Valor de PSN no válido")
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0

    return encrypted_message, orderPsn

# Funcion de Desencriptacion
def decrypt(encrypted_message, keys, psn):
    decrypted_message = []
    key_index = 0
    psn_index = 0

    for index, char_code in enumerate(encrypted_message):

        key = keys[key_index]
        psn_value = psn[psn_index]
        if  psn_value == 0:
            decrypted_char_code = methods.reverse_fk1(char_code, key)
        elif  psn_value == 1:
            decrypted_char_code = methods.reverse_fk2(char_code, key)
        elif psn_value == 2:
            decrypted_char_code = methods.reverse_fk3(char_code, key)
        else:
            raise ValueError("Valor de PSN no válido")
        
        decrypted_char = chr(decrypted_char_code)
        decrypted_message += decrypted_char
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0

        psn_index += 1
        if psn_index >= len(psn):
            psn_index = 0
        
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
    #psn = utils.select_psn(message)  # Selecciona PSN en base al mensaje
    
    encrypted_message , psn = encrypt(message, keys)
    decrypted_message = decrypt(encrypted_message, keys, psn)
    
    ft_message = format_message('{:06d}'.format(1), '{:04d}'.format(1), encrypted_message , psn[0])
    save_message('results/RM_Server_result.txt', ft_message)
    
    
    print("Client Encrypted Message:", encrypted_message)
    print("Decrypted Server Message:", decrypted_message)