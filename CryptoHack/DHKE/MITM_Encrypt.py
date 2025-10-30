from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
from secret import shared_secret

FLAG = b'crypto{????????????????????????????}'

def encrypt_flag(shared_secret: int):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    data = {}
    data['iv'] = iv.hex()
    data['encrypted_flag'] = ciphertext.hex()
    return data

print(encrypt_flag(shared_secret))
