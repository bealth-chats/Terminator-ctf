import math

with open('message.txt', 'r') as f:
    exec(f.read())

p = math.gcd(N1, N2)
q1 = N1 // p
q2 = N2 // p

def ext_euclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = ext_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inv(a, m):
    gcd, x, y = ext_euclid(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

phi1 = (p - 1) * (q1 - 1)
d1 = mod_inv(e, phi1)
m1 = pow(ct1, d1, N1)

phi2 = (p - 1) * (q2 - 1)
d2 = mod_inv(e, phi2)
m2 = pow(ct2, d2, N2)

part1 = m1.to_bytes((m1.bit_length() + 7) // 8, 'big')
part2 = m2.to_bytes((m2.bit_length() + 7) // 8, 'big')

# Extract flag
# m1: b"&\x18\xcbV\x8cx\xd5\xdc2b\xff'x\xc8\x82\x00t3rmctf{h4kun4_sh4mb4_ngu"
# m2: b'mu_in4y0shind4_j3mb3_69c}\xa7\xb0\xcd\x1ca]5&8QeH\x1bo\xe2t'
# Flag: t3rmctf{h4kun4_sh4mb4_ngumu_in4y0shind4_j3mb3_69c}
print(part1[16:].decode() + part2[:25].decode())
