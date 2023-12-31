# First Contact Message (FCM)
# Este programa genera las tablas de llaves que se usaran para la encriptacion y genera un txt de conexion en el cual se especifica el id, tipo de mensaje, payload y psn

from functions import methods
import utils

if __name__ == "__main__":
    P , Q , S = utils.pqs_generator()
    
    key_number = input("Ingrese numero de llaves a generar: ")

    #keys = utils.key_table_generator(P,Q,S,int(key_number))
    keys = [utils.generate_key(P , Q , S + i) for i in range(int(key_number))]
    ft_message = utils.format_message('{:06d}'.format(1), '{:04d}'.format(0) , [P, Q, S, int(key_number)], 'N/A')
    utils.save_message('results/response.txt',ft_message)

    
    # Guardar la tabla de llaves en un archivo
    with open("results/keys.txt", "w") as file:
        for i, key in enumerate(keys, 1):
            file.write(f"Numero de llave {i}: {key}\n")

    print("Tabla de llaves guardada en results/keys.txt")
    print("Datos de Conexion guardado en results/response.txt")
