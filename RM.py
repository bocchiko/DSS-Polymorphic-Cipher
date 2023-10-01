from functions import methods
import re
import utils

# Decryption function
def decrypt(encrypted_message, keys, psn):
    decrypted_message = []
    key_index = 0
    psn_index = 0
    for index, char_code in enumerate(encrypted_message):

        key = keys[key_index]
        psn_value = psn[psn_index]
        if  psn_value == 0:
            print('entre 0')
            decrypted_char_code = methods.reverse_fk1(char_code, key)
        elif  psn_value == 1:
            print('entre 1')
            decrypted_char_code = methods.reverse_fk2(char_code, key)
        elif psn_value == 2:
            print('entre 2')
            decrypted_char_code = methods.reverse_fk3(char_code, key)
        elif psn_value == 3:
            print('entre 3')
            decrypted_char_code = methods.reverse_fk4(char_code, key)
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

""" # Decryption function
def decrypt(encrypted_message, keys, psn):
    decrypted_message = []
    key_index = 0
    
    for char_code in encrypted_message:
        key = keys[key_index]
        decrypted_char_code = methods.apply_reversible_functions(char_code, key, psn)
        # Ensure the decrypted character code is within the valid Unicode range
        decrypted_char_code %= 0x110000
        decrypted_message.append(chr(decrypted_char_code))
        
        key_index += 1
        if key_index >= len(keys):
            key_index = 0
    
    return ''.join(decrypted_message)
 """
def extract_message_components():
    with open('results/Server_Result.txt','r') as file:
        result_file = file.read()

    lines = result_file.strip().split('\n')
    id = (lines[0].split(': ')[1])
    type = (lines[1].split(': ')[1])
    payload = (lines[2].split(': ')[1])
    payloadListInt = list(map(int,re.findall(r'(\d+)', payload)))
    psn = (lines[3].split(': ')[1])
    psnListInt = list(map(int,re.findall(r'(\d+)', psn)))
    encrypted_message = (lines[4].split(': ')[1])
    encrypted_messageListInt = list(map(int,re.findall(r'(\d+)', encrypted_message)))

    return int(id), int(type), payloadListInt, psnListInt, encrypted_messageListInt

def extract_key_components():
    with open('results/Llaves.txt', 'r') as file:
        text = file.read()

    file_keys = list(map(int,re.findall(r': (\d+)', text) ))
    return file_keys 

if __name__ == "__main__":
    
    id, type , payload, psn , encrypted_message = extract_message_components()
    keys = extract_key_components()
    #print(len(psn))
    decrypt_message = decrypt(encrypted_message,keys,psn)
    print('Decripted Message: ',decrypt_message)