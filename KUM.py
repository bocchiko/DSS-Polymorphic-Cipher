# Key Update Message (KUM)
# Este programa es para actualizar las llaves creadas en el programa FCM
# El programa cuenta las llaves existentes para generar la misma cantidad de llaves.
# Actualiza los archivos de llaves.txt y conexion.txt detallando el id, tipo de mensaje, payload y psn

from functions import methods
import utils

def format_message(id, type, payload, psn):
    return f"{id}\n{type}\n{payload}\n{psn}"
    
# Guardar datos de conexion
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)

if __name__ == "__main__":
    P , Q , S = utils.pqs_generator()
    
    # Cuenta cuantas llaves existen para generar la misma cantidad de llaves
    with open("results/llaves.txt", "r") as file:
        existing_keys = file.readlines()
        key_number = len(existing_keys)

    keys = utils.key_table_generator(P,Q,S,int(key_number))

    ft_message = format_message('{:06d}'.format(1), str(10).zfill(4), [P, Q, S, int(key_number)], 'N/A')
    with open("results/conexion.txt", "w") as file:
        file.write(ft_message)
    
    # Realiza la actualizacion de las llaves
    with open("results/llaves.txt", "w") as file:
        for i, key in enumerate(keys, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves actualizada en results/llaves.txt")
    print("Datos de Conexion actualizados en results/conexion.txt")


