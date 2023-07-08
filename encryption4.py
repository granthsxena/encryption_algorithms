import math

def encrypt(text, key):
    num_columns = math.ceil(len(text) / key)
    encrypted_text = ""
    for col in range(num_columns):
        pointer = col
        while pointer < len(text):
            encrypted_text += text[pointer]
            pointer += num_columns
    return encrypted_text

def decrypt(encrypted_text, key):
    num_columns = math.ceil(len(encrypted_text) / key)
    num_rows = math.ceil(len(encrypted_text) / num_columns)
    decrypted_text = ""
    for col in range(num_columns):
        pointer = col
        while pointer < len(encrypted_text):
            decrypted_text += encrypted_text[pointer]
            pointer += num_columns
    return decrypted_text
