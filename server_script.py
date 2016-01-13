from socket import socket, AF_INET, SOCK_STREAM
from settings import password, port
import os


myHost = ''
max_connections = 0
dataChunk = 1024

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, port))
sockobj.listen(max_connections)

while True:
    con, address = sockobj.accept()
    while True:
        data = con.recv(dataChunk)
        if not data: break
        if data == password:
            pipe = os.popen('df -h')
            df_b = pipe.read().encode()
            con.send(df_b)
    con.close()
sockobj.close()
