import socket
from cryptography.fernet import Fernet

s = socket.socket()
port = 5050
ip = '172.16.36.8'
s.connect((ip, port))

# with open("Key.key", "rb") as r:
#     key = r.read()
#     r.close()

key = b'3MTnubxhjkBA3sW8M_mvzahIXTVtrgKudUi0iqAl4hk='

f = Fernet(key)
dmsg = f.decrypt(s.recv(1024))
print(dmsg.decode('utf-8'))