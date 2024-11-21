M = "криптографія"
height = 2

def encrypt(plaintext, key):
    init_list = []
    cryptotext = ""

    for i in range (key, 0, -1):
        text = plaintext[i-1::key]
        cryptotext += text
    return cryptotext

def decrypt(cryptotext, key):
    return encrypt(cryptotext, len(cryptotext) // key)[::-1]

C = encrypt(M, height)
print(C)
M1 = decrypt(C, height)
print(M1)
print(M == M1)
