import string
print(string.ascii_uppercase)
alphabet = list(string.ascii_lowercase)

M = "plaintext"
height = 3

def encrypt(plaintext, key):
    crypto = ""

    for char in plaintext:
        char_index = alphabet.index(char)
        new_char_index = (char_index + key) % len(alphabet)
        new_char = alphabet[new_char_index]
        crypto += new_char
    return crypto

def decrypt(plaintext, key):
    return encrypt(plaintext, -key)

C = encrypt(M, height)
print(C)
M1 = decrypt(C, height)
print(M1)
print(M1 == M)
