def encrypt_with_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(message, monoalpha_cipher):
    inverse_monoalpha = {v: k for k, v in monoalpha_cipher.items()}
    decrypted_message = []
    for letter in message:
        decrypted_message.append(inverse_monoalpha.get(letter, letter))
    return ''.join(decrypted_message)

plaintext = 'hello world'
ciphertext_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
plaintext_alphabet = 'abcdefghijklmnopqrstuvwxyz'
monoalpha_cipher = dict(zip(plaintext_alphabet, ciphertext_alphabet))
ciphertext = encrypt_with_monoalpha(plaintext, monoalpha_cipher)
decrypted_plaintext = decrypt_with_monoalpha(ciphertext, monoalpha_cipher)
print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)
print('Decrypted plaintext:', decrypted_plaintext)
