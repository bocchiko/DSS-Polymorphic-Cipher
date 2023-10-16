import random

# FUNCIONES SCRAMBLE, GENERATION Y MUTATION

# Esta función toma dos argumentos x e y 
# y realiza una operación XOR (bitwise exclusive OR) entre ellos.
def scramble(x, y):
    return (x ^ y) 

# Esta función realiza dos operaciones XOR. Primero, realiza un XOR entre x e y. 
# Luego realiza un XOR entre el resultado anterior y una constante (por defecto, 1).
def generation(x, y,constant=1):
    result = (x ^ y) ^ constant
    return result

# Esta función realiza una rotación a la izquierda de y en shift bits (por defecto, 2). 
# Luego, realiza una operación XOR entre x e y después de la rotación.
def mutation(x, y, shift=2):
    y = (y << shift) | (y >> (64 - shift))  # Rotate y left by 'shift' bits
    result = x ^ y
    return result



# FUNCIONES FK PARA CIFRADO DE MENSAJES

# Esta función toma dos argumentos x y key, y llama a la función scramble(x, key) para realizar una operación XOR entre ellos.
def fk1(x, key):
    return scramble(x, key)

# Esta función toma tres argumentos x, key, y psn. Llama a la función generation(x, key, psn) para realizar dos operaciones XOR. 
# Primero, realiza un XOR entre x e key, y luego realiza un XOR entre el resultado anterior y psn.
def fk2(x, key,psn):
    return generation(x, key, psn)

# Esta función toma tres argumentos x, key, y psn. 
# Llama a la función mutation(x, key, psn) para realizar una rotación a la izquierda en key,
# luego realiza una operación XOR entre x y el resultado de la rotación. 
def fk3(x, key, psn):
    return mutation(x, key,psn)


# FUNCIONES Fs, Fg y Fm

# Esta función toma dos argumentos x e y y realiza dos operaciones XOR. 
# Primero, realiza un XOR entre x e y, y luego realiza un XOR entre el resultado anterior y un desplazamiento a la derecha en x en un bit. 
def fs(x, y):
    return (x ^ y) ^ (x >> 1)

# Esta función toma dos argumentos x e y y realiza dos operaciones XOR. 
# Primero, realiza un XOR entre x e y, y luego realiza un XOR entre el resultado anterior y un desplazamiento a la izquierda en x en un bit.
def fg(x, y):
    return (x & y) ^ (x << 1)

# Esta función toma dos argumentos x e y y realiza dos operaciones XOR. 
# Primero, realiza un XOR entre x e y, y luego realiza un XOR entre el resultado anterior y un desplazamiento a la derecha en y en un bit.
def fm(x, y):
    return (x | y) ^ (y >> 1)