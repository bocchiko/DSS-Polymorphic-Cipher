# Regular Message (RM)
# Este programa es para encriptar y desencriptar mensajes. Este programa lee el txt con la tabla de llaves para encriptar y desencriptar un mensaje
# El resultado de encriptacion y desencriptacion se muestra en la consola 

from functions import methods
import utils

# Funcion de Encriptacion
def encrypt(message, keys):
    encrypted_message = []  # Inicializa una lista para almacenar el mensaje cifrado
    key_index = 0 # Inicializa el índice de clave en 0
    orderPsn = [] # Inicializa una lista para almacenar el orden de PSN de cada carácter en el mensaje
    
    for char in message:
        key = keys[key_index] # Obtiene la clave correspondiente
        psn = utils.select_psn(char) # Selecciona el PSN para el carácter
        char_ord = ord(char) # Obtiene el valor numérico del carácter

        # dependiendo del valor de psn, se cifra el carácter de una de las tres formas posibles. 
        # Estas tres formas de cifrado son representadas por las funciones methods.fk1, methods.fk2, y methods.fk3. 
        # La función apropiada se elige según el valor de psn y se utiliza para cifrar el carácter.
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
        
        key_index += 1 # Avanza al siguiente índice de clave
        if key_index >= len(keys):
            key_index = 0

    return encrypted_message, orderPsn

# Funcion de Desencriptacion
def decrypt(encrypted_message, keys, psn):
    decrypted_message = [] # Inicializa una lista para almacenar el mensaje cifrado
    key_index = 0 # Inicializa el índice de clave en 0
    psn_index = 0 # Inicializa una lista para almacenar el orden de PSN de cada carácter en el mensaje

    # Dependiendo del valor de psn_value, el carácter cifrado se descifra utilizando una de las tres funciones de descifrado posibles: methods.fk1, methods.fk2 o methods.fk3. 
    # La función apropiada se selecciona según el valor de psn_value y se utiliza para realizar el descifrado.
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
        
        # El resultado del descifrado se almacena en decrypted_char_code, que representa el valor numérico del carácter descifrado.
        # chr(decrypted_char_code) convierte el valor numérico del carácter descifrado de nuevo a su representación de carácter.
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

    # Obtiene las llaves del archivo keys.txt
    keys = []
    with open("results/keys.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(": ")
            if len(parts) == 2:
                key = int(parts[1])
                keys.append(key)
    
    message = input("Ingrese el mensaje a cifrar (máximo 64 caracteres): ")
    
    encrypted_message , psn = encrypt(message, keys)  # Cifra el mensaje
    decrypted_message = decrypt(encrypted_message, keys, psn) # Descifra el mensaje
    
    # Formatea el mensaje cifrado y lo guarda en un archivo
    ft_message = utils.format_message('{:06d}'.format(1), '{:04d}'.format(1), encrypted_message , psn)
    utils.save_message('results/response.txt', ft_message)
    
    print("Client Encrypted Message:", encrypted_message)
    print("Decrypted Server Message:", decrypted_message)