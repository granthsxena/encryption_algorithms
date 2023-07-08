import random

def generate_key():
    chars = [chr(i) for i in range(32, 127)]
    random.shuffle(chars)
    key = "".join(chars)
    return key

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in key:
            index = key.index(char)
            encrypted_text += chr(index + 32)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        index = ord(char) - 32
        decrypted_text += key[index]
    return decrypted_text
