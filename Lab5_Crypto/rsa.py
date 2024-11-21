import random
from sympy import primerange, isprime

def generate_prime_number(lower, upper):
    primes = list(primerange(lower, upper))
    return random.choice(primes)

def generate_keys():
    p = generate_prime_number(63, 127)
    q = generate_prime_number(63, 127)
    while p == q:
        q = generate_prime_number(63, 127)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 23**2
    if e >= phi or gcd(e, phi) != 1:
        raise ValueError("e must be co-prime to phi(n) and less than phi(n)")

    d = modinv(e, phi)

    return (e, n), (d, n)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plain_text, public_key):
    e, n = public_key
    cipher_text = pow(plain_text, e, n)
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = pow(cipher_text, d, n)
    return plain_text

def main():
    public_key, private_key = generate_keys()

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    M = 100

    cipher_text = encrypt(M, public_key)
    print(f"Cipher Text: {cipher_text}")

    plain_text = decrypt(cipher_text, private_key)
    print(f"Plain Text: {plain_text}")

if __name__ == "__main__":
    main()
