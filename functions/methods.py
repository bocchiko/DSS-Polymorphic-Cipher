#solo probando
def scramble2(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256
def generation2(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256
def mutation2(x, y, reverse=False):
    if reverse:
        return (x - y) % 256
    return (x + y) % 256

# funciones de encriptación
def fk1(x, key):
    return scramble2(x, key)

def fk2(x, key):
    return generation2(x, key)

def fk3(x, key):
    return mutation2(x, key)


#funciones de desincriptacion
def reverse_fk1(x,key):
    return scramble2(x,key,reverse=True)

def reverse_fk2(x,key):
    return generation2(x,key,reverse=True)

def reverse_fk3(x,key):
    return mutation2(x,key,reverse=True)
