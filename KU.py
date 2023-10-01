import utils
import re

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

if __name__ == "__main__":

    id, type , payload, psn , encrypted_message = extract_message_components()
    
    N = payload[3]
    P , Q , S = utils.pqs_generator()
    keys_updated = utils.key_table_generator(P, Q ,S ,N)
    #print(keys_updated)

    with open("results/Llaves.txt", "w") as file:
        for i, key in enumerate(keys_updated, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves actualizada en results/Llaves.txt")