# First Contact Message (FCM)
# Este programa genera las tablas de llaves que se usaran para la encriptacion y genera un txt de conexion en el cual se especifica el id, tipo de mensaje, payload y psn

from functions import methods
import utils

# Funcion para formatear el mensaje con id, tipo, payload y psn
def format_message(id, type, payload, psn):
    return f"{id}\n{type}\n{payload}\n{psn}"
    
# Guardar el mensaje encriptado en un archivo
def save_message(filename, formatted_message):
    with open(filename, "w") as file:
        file.write(formatted_message)

if __name__ == "__main__":
    P , Q , S = utils.pqs_generator()
    
    key_number = input("Ingrese numero de llaves a generar: ")

    keys = utils.key_table_generator(P,Q,S,int(key_number))

    ft_message = format_message('{:06d}'.format(1), 'FCM', [P, Q, S, int(key_number)], 'N/A')
    with open("results/conexion.txt", "w") as file:
        file.write(ft_message)
    
    # Guardar la tabla de llaves en un archivo
    with open("results/llaves.txt", "w") as file:
        for i, key in enumerate(keys, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves guardada en results/llaves.txt")
    print("Datos de Conexion guardado en results/conexion.txt")
