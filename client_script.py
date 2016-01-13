from socket import socket, AF_INET, SOCK_STREAM
from settings import password, port

serverHost = ''
dataChunk = 1024

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, port))
sockobj.send(password)
data = sockobj.recv(dataChunk).decode()
print(data)
sockobj.close()
