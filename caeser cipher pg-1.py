def caesar_encrypt(message, key):
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 65 + key) % 26 + 65)
            encrypted_message += shifted_letter
        else:
            encrypted_message += letter
    return encrypted_message

def caesar_decrypt(message, key):
    decrypted_message = ""
    for letter in message:
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 65 - key) % 26 + 65)
            decrypted_message += shifted_letter
        else:
            decrypted_message += letter
    return decrypted_message

message = input("Enter a message: ")
key = int(input("Enter a key (1-25): "))

encrypted_message = caesar_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
