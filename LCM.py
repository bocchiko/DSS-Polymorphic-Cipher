# Last Contact Message (LCM)
# Programa para terminar comunicacion y barrar las llaves generadas y txt de conexion.

import os
import utils
# Función para borrar un archivo si existe
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Archivo {filename} borrado con éxito.")
    else:
        print(f"El archivo {filename} no existe.")

if __name__ == "__main__":
    # Lista de archivos a borrar
    files_to_delete = [
        "results/keys.txt",
    ]

    deleted_any_file = False

    for file in files_to_delete:
        if os.path.exists(file):
            delete_file(file)
            deleted_any_file = True
    
    # Genera un mensaje LCM para indicar el cierre de la comunicación
    ft_message = utils.format_message('{:06d}'.format(1), '{:04d}'.format(11) , 'N/A', 'N/A')
    utils.save_message('results/response.txt',ft_message)

    print("Datos de Conexion guardado en results/response.txt")

    if not deleted_any_file:
        print("No existe comunicación existente con el servidor. Comienza una nueva comunicación por medio de FCM")