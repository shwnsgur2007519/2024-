import random

def rotate(a, l):
    return ((a << 1) | (a >> (l - 1))) & ((1 << l) - 1)

def conv(a, b, l):
    XOR = 0
    while b:
        if b & 1:
            XOR ^= a
        a = rotate(a, l)
        b >>= 1
    return XOR

def pow(a, b, l):
    
    result = 1
    while b:
        if b % 2 == 1:
            result = conv(result, a, l)
        a = conv(a, a, l)
        b //= 2
    
    return result

# k=2**2053
# result_bin = pow(random.randint(1,k), k, k)
# print("Binary result:", result_bin)

