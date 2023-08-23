def encrypt_block(plaintext):
    return plaintext

def decrypt_block(ciphertext):
    return ciphertext

def simulate_transmitted_ciphertext_error(ciphertext, block_index):
    ciphertext[block_index] = chr(ord(ciphertext[block_index]) ^ 0x01)

def main():
    P1 = "Hello, this is P1."
    P2 = "And this is P2."
    C1 = encrypt_block(P1)
    C2 = encrypt_block(P2)

    print("ECB Mode:")
    print("Original C1:", C1)
    print("Original C2:", C2)

    C1_error = list(C1)
    simulate_transmitted_ciphertext_error(C1_error, 5)
    C1_error = ''.join(C1_error)
    print("Transmitted C1 with error:", C1_error)

    P1_error = decrypt_block(C1_error)
    print("Decrypted P1 (with error):", P1_error)

    P2_decrypted = decrypt_block(C2)
    print("Decrypted P2:", P2_decrypted)

if __name__ == "__main__":
    main()
