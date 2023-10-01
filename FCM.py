from functions import methods
import utils


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
        elif psn == 3:
            orderPsn.append(psn)
            encrypted_char_code = methods.fk4(char_code, key)
            encrypted_message.append(encrypted_char_code )
        else:
            raise ValueError("Valor de PSN no válido")
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0

    return encrypted_message, orderPsn

""" def encrypt(message, keys, psn):
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
 """

def format_message(id, type, payload, psn,encrypted_message):
    return f"ID: {id}\nTipo: {type}\nPayload: {(payload)}\nPSN: {psn}\nMensaje Encriptado: {encrypted_message}"

# Guardar el mensaje encriptado en un archivo
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)

if __name__ == "__main__":
    P , Q , S = utils.pqs_generator()
    print(P,Q,S)
    key_number = input("Ingrese numero de llaves a generar: ") #keys = [generate_key(P , Q , S + i) for i in range(int(key_number))]
    
    keys = utils.key_table_generator(P , Q, S, int(key_number))
    message = input("Ingrese el mensaje a cifrar (máximo 64 caracteres): ")
    #print(keys)
    encrypted_message,psn = encrypt(message, keys)

    ft_message = format_message('{:06d}'.format(1), '{:04d}'.format(0), [P, Q, S, int(key_number)], psn, encrypted_message)
    save_message('results/Server_Result.txt', ft_message)
    
    # Guardar la tabla de llaves en un archivo
    with open("results/Llaves.txt", "w") as file:
        for i, key in enumerate(keys, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves guardada en results/FCM_Server_result.txt")
    print("Mensaje encriptado guardado en results/FCM_Server_result.txt")
