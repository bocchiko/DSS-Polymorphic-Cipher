# Key Update Message (KUM)
# Este programa es para actualizar las llaves creadas en el programa FCM
# El programa cuenta las llaves existentes para generar la misma cantidad de llaves.
# Actualiza los archivos de llaves.txt y conexion.txt detallando el id, tipo de mensaje, payload y psn

from functions import methods
import utils


if __name__ == "__main__":
    P , Q , S = utils.pqs_generator()
    
    # Cuenta cuantas llaves existen para generar la misma cantidad de llaves
    with open("results/keys.txt", "r") as file:
        existing_keys = file.readlines()
        key_number = len(existing_keys)

    keys = utils.key_table_generator(P,Q,S,int(key_number))
    
    ft_message = utils.format_message('{:06d}'.format(1), '{:04d}'.format(3), [P, Q, S, int(key_number)], 'N/A')
    utils.save_message('results/response.txt',ft_message)
    
    # Realiza la actualizacion de las llaves
    with open("results/keys.txt", "w") as file:
        for i, key in enumerate(keys, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves actualizada en results/keys.txt")
    print("Datos de Conexion actualizados en results/response.txt")


