#!/usr/bin/env python3

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)

text = 'hello world'.encode()
encr = cipher.encrypt(text)
print(encr)

decr = cipher.decrypt(encr)
print(decr)
