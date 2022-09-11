import base64
import hashlib
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()

if(not os.path.exists('key.hkey')):
    with open('key.hkey', 'wb') as filekey:
        filekey.write(key)
else:
    with open('key.hkey', 'rb') as filekey:
        key = filekey.read()

def encrypt(raw):
    fernet = Fernet(key)
    return fernet.encrypt(raw)

def decrypt(cipher):
    fernet = Fernet(key)
    return fernet.decrypt(cipher)

def sha256sum(filename):
    if os.path.isdir(filename):
        return;
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

