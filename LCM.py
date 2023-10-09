# Last Contact Message (LCM)
# Programa para terminar comunicacion y barrar las llaves generadas y txt de conexion.

import os

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
        "results/conexion.txt",
        "results/llaves.txt",
        "results/RM_Server_result.txt",  
    ]

    deleted_any_file = False

    for file in files_to_delete:
        if os.path.exists(file):
            delete_file(file)
            deleted_any_file = True

    if not deleted_any_file:
        print("No existe comunicación existente con el servidor. Comienza una nueva comunicación por medio de FCM")