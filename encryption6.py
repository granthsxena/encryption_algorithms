from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

def encrypt_aes_ctr(plaintext, key):
    nonce = get_random_bytes(8)
    counter = Counter.new(64, nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    ciphertext = cipher.encrypt(plaintext)
    return nonce + ciphertext

def decrypt_aes_ctr(ciphertext, key):
    nonce = ciphertext[:8]
    ciphertext = ciphertext[8:]
    counter = Counter.new(64, nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
