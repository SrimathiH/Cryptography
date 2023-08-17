import string

def gcd(a, b):
    # Calculate the greatest common divisor of a and b
    while b != 0:
        a, b = b, a % b
    return a

def generate_key(a, b):
    # Generate a key for the affine Caesar cipher
    if gcd(a, 26) != 1:
        return None
    return a, b

def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the affine Caesar cipher
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            index = ord(letter) - base
            a, b = key
            a_inv = 0
            for i in range(26):
                if (a * i) % 26 == 1:
                    a_inv = i
                    break
            index = (a_inv * (index - b)) % 26
            plaintext += chr(base + index)
        else:
            plaintext += letter
    return plaintext

# Example usage
ciphertext = 'BUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUBUB'
freq1 = 'B'
freq2 = 'U'
for a in range(1, 26):
    if gcd(a, 26) == 1:
        for b in range(26):
            key = generate_key(a, b)
            if key is not None:
                plaintext = decrypt(ciphertext, key)
                if freq1 in plaintext and freq2 in plaintext:
                    print('Key:', key)
                    print('Plaintext:', plaintext)
