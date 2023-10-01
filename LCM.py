import os

if __name__ == "__main__":
    
    # Specify the file path you want to delete
    file_path_server = "results/Server_Result.txt"  # Replace with the actual path of the file
    file_path_keys = "results/Llaves.txt"
    try:
        # Attempt to remove the file
        os.remove(file_path_server)
        os.remove(file_path_keys)
        print("Tabla de llaves eliminada de results/Server_Server_result.txt")
        print("Mensaje encriptado eliminado de results/Server_result.txt")

    except FileNotFoundError:

        print(f"File '{file_path_server}' no se encontro.")
        print(f"File '{file_path_keys}' no se encontro.")

    except Exception as e:

        print(f"An error occurred: {str(e)}")
    