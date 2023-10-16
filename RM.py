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
        psn = utils.select_psn(char)
        char_ord = ord(char)
        if psn == 0:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk1(char_ord, key)
            encrypted_message.append(encrypted_char_code )
        elif psn == 1:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk2(char_ord, key, psn)
            encrypted_message.append(encrypted_char_code )
        elif psn == 2:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk3(char_ord, key, psn)
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
            decrypted_char_code = methods.fk1(char_code, key)
        elif  psn_value == 1:
            decrypted_char_code =  methods.fk2(char_code, key, psn_value)
        elif psn_value == 2:
            decrypted_char_code = methods.fk3(char_code, key, psn_value)
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

if __name__ == "__main__":

    keys = []
    with open("results/keys.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(": ")
            if len(parts) == 2:
                key = int(parts[1])
                keys.append(key)
    
    message = input("Ingrese el mensaje a cifrar (máximo 64 caracteres): ")
    #psn = utils.select_psn(message)  # Selecciona PSN en base al mensaje
    #message = message[:64] Lorem Ipsum is simply dummy text of the printing and typesetting
    encrypted_message , psn = encrypt(message, keys)
    decrypted_message = decrypt(encrypted_message, keys, psn)
    
    ft_message = utils.format_message('{:06d}'.format(1), '{:04d}'.format(1), encrypted_message , psn)
    utils.save_message('results/response.txt', ft_message)
    
    print("Client Encrypted Message:", encrypted_message)
    print("Decrypted Server Message:", decrypted_message)