cyrillic_alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]

alphabet_dict = {letter: i for i, letter in enumerate(cyrillic_alphabet)}

M = "криптографічнiметодизахистуінформації"
key = "Івасюк"

def encrypt(plaintext, key):
    crypto = ""
    if len(key) < len(plaintext):
        key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        key_char = key[i]
        if plain_char in alphabet_dict and key_char in alphabet_dict:
            plain_index = alphabet_dict[plain_char]
            key_index = alphabet_dict[key_char]
            cipher_index = (plain_index + key_index) % len(cyrillic_alphabet)
            crypto += cyrillic_alphabet[cipher_index]
        else:
            crypto += plain_char

    return crypto

def decrypt(cryptotext, key):
    plain = ""
    if len(key) < len(cryptotext):
        key = key * (len(cryptotext) // len(key)) + key[:len(cryptotext) % len(key)]

    for i in range(len(cryptotext)):
        crypto_char = cryptotext[i]
        key_char = key[i]
        if crypto_char in alphabet_dict and key_char in alphabet_dict:
            crypto_index = alphabet_dict[crypto_char]
            key_index = alphabet_dict[key_char]
            plain_index = (crypto_index - key_index) % len(cyrillic_alphabet)
            plain += cyrillic_alphabet[plain_index]
        else:
            plain += crypto_char

    return plain

C = encrypt(M, key)
print(C)
M1 = decrypt(C, key)
print(M1)
print(M == M1)
