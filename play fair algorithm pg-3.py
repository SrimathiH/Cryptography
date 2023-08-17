import string

def generate_matrix(key):
    # Create a 5x5 matrix using the key
    key = key.upper().replace('J', 'I')
    alphabet = string.ascii_uppercase.replace('J', '')
    matrix = []
    for letter in key + alphabet:
        if letter not in matrix and len(matrix) < 25:
            matrix.append(letter)
    return matrix

def get_indices(letter, matrix):
    # Get the row and column indices of a letter in the matrix
    index = matrix.index(letter)
    row = index // 5
    col = index % 5
    return row, col

def encrypt(plaintext, key):
    # Encrypt the plaintext using the Playfair algorithm
    matrix = generate_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = ''.join(filter(str.isalpha, plaintext))
    if len(plaintext) % 2 == 1:
        plaintext += 'X'
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        a_row, a_col = get_indices(a, matrix)
        b_row, b_col = get_indices(b, matrix)
        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5
        else:
            a_col, b_col = b_col, a_col
        ciphertext += matrix[a_row*5+a_col]
        ciphertext += matrix[b_row*5+b_col]
    return ciphertext

# Example usage
key = 'secret'
plaintext = 'hello world'
ciphertext = encrypt(plaintext, key)
print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)
