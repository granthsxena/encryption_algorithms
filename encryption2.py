import random

def generate_key(length):
    key = ""
    for _ in range(length):
        key += chr(random.randint(32, 126))
    return key

def encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    for char in text:
        key_char = key[key_index % len(key)]
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted_text += encrypted_char
        key_index += 1
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        key_char = key[key_index % len(key)]
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted_text += decrypted_char
        key_index += 1
    return decrypted_text
