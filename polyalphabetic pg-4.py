import string

def generate_key(key, length):
    
    key = key.upper().replace('J', 'I')
    alphabet = string.ascii_uppercase.replace('J', '')
    full_key = key
    while len(full_key) < length:
        full_key += alphabet
    return full_key[:length]

def encrypt(plaintext, key):
    
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = ''.join(filter(str.isalpha, plaintext))
    key = generate_key(key, len(plaintext))
    ciphertext = ''
    for i in range(len(plaintext)):
        shift = ord(key[i]) - ord('A')
        ciphertext += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
    return ciphertext

key = 'secret'
plaintext = 'hello world'
ciphertext = encrypt(plaintext, key)
print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)
