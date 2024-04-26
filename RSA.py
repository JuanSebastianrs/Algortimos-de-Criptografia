import random
from math import gcd

def divide_blocks(message, block_size):
    blocks = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    return blocks

def letter_ascii(message):
    message_ascii = [str(ord(letter)).zfill(3) for letter in message]
    return message_ascii

def ascii_letter(message_ascii):
    ascii_str = str(message_ascii)
    message = "".join([chr(int(ascii_str[i:i+3])) for i in range(0, len(ascii_str), 3)])
    return message

def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception('The modular inverse does not exist.')

def genLlaves(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    g = maximo_comun_divisor(phi, e)
    while g != 1:
        e = random.randrange(2, phi)
        g = maximo_comun_divisor(phi, e)
    d = find_mod_inv(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(x, kpub):
    e, n = kpub
    y = pow(x, e, n)
    return y

def rsa_decrypt(y, kpriv):
    d, n = kpriv
    x = pow(y, d, n)
    return x

def main():
    p = 17
    q = 19
    public, private = genLlaves(p, q)
    print("Public key:", public)
    print("Private key:", private)
    message = "Johan cacorro"
    print("Original message:", message)
    ascii_msg = letter_ascii(message)
    print("ASCII representation:", ascii_msg)
    blocks = [int(block) for block in ascii_msg]  
    print("Blocks:", blocks)
    encrypted_blocks = [rsa_encrypt(block, public) for block in blocks]
    print("Encrypted blocks:", encrypted_blocks)
    decrypted_blocks = [rsa_decrypt(block, private) for block in encrypted_blocks]
    print("Decrypted blocks:", decrypted_blocks)
    decrypted_msg = "".join([chr(block) for block in decrypted_blocks])
    print("Decrypted message:", decrypted_msg)

if __name__ == "__main__":
    main()
