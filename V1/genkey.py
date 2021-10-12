from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("Key.key", "wb") as f:
    f.write(key)
    f.close()