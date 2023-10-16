def scramble(x, y):
    return (x ^ y) 

def generation(x, y,constant=1):
    result = (x ^ y) ^ constant
    return result

def mutation(x, y, shift=2):
    y = (y << shift) | (y >> (64 - shift))  # Rotate y left by 'shift' bits
    result = x ^ y
    return result

def fk1(x, key):
    return scramble(x, key)

def fk2(x, key,psn):
    return generation(x, key, psn)

def fk3(x, key, psn):
    return mutation(x, key,psn)


def fs(x, y):
    return (x ^ y) ^ (x >> 1)

def fg(x, y):
    return (x & y) ^ (x << 1)

def fm(x, y):
    return (x | y) ^ (y >> 1)

