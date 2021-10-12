import socket
from cryptography.fernet import Fernet

s = socket.socket()
port = 5050
ip = '172.16.36.8'

s.bind((ip, port))

s.listen(5)
print("Socket is listening")

with open("Key.key", "rb") as r:
    key = r.read()
    r.close()

f = Fernet(key)
token = input('Message to be sent: ').encode('utf-8')
emsg = f.encrypt(token)
print(f"Encrytped messahed {emsg.decode('utf-8')}")

# print(token)

while True:
    c, addr = s.accept()
    print("Got a connection from ", addr)
    c.send(emsg)
    print("Sent a message")
    c.close()
