#solo probando
def scramble(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256
def generation(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256
def mutation(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256

""" def scramble(x, y, reverse=False):
    if reverse:
        return x ^ (x >> 1) ^ y
    return (x ^ y) ^ (x >> 1)
def generation(x, y, reverse=False):
    if reverse:
        return (x & y) ^ (x >> 1)
    return (x & y) ^ (x << 1)
def mutation(x, y, reverse=False):
    if reverse:
        return (x | y) ^ (y << 1) 
    return (x | y) ^ (y >> 1) """

# Reversible functions (you can implement these based on your requirements)
""" def scramble(x, y):
    return (x ^ y) ^ (x >> 1)

def generation(x, y):
    return (x & y) ^ (x << 1)

def mutation(x, y):
    return (x | y) ^ (y >> 1)

def reverse_scramble(x, y):
    return x ^ (x >> 1) ^ y

def reverse_generation(x, y):
    return (x & y) ^ (x >> 1)

def reverse_mutation(x, y):
    return (x | y) ^ (y << 1) """

# funciones de encriptación
def fk1(x, key):
    return scramble(x, key)

def fk2(x, key):
    return generation(x, key)

def fk3(x, key):
    return mutation(x, key)

def fk4(x, key):
    return scramble(x, key)

#funciones de desincriptacion
def reverse_fk1(x,key):
    return scramble(x,key,reverse=True)

def reverse_fk2(x,key):
    return generation(x,key,reverse=True)

def reverse_fk3(x,key):
    return mutation(x,key,reverse=True)

def reverse_fk4(x,key):
    return scramble(x,key,reverse=True)