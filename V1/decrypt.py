import socket
from cryptography.fernet import Fernet

s = socket.socket()
port = 5050 #Change if you want, if you do change it pick a port above 1024. Must be the same in encrypt.py
ip = #replace with server ip e.g. '1.1.1.1' Must be the same in encrypt.py
s.connect((ip, port))

with open("Key.key", "rb") as r:
    key = r.read()
    r.close()

f = Fernet(key)
dmsg = f.decrypt(s.recv(1024))
print(dmsg.decode('utf-8'))
