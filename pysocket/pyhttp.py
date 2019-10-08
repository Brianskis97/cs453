#! /usr/bin/python3

import socket

ip = '204.15.135.8'
port = 80

address = (ip, port)

cnct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnct.connect(address)

cnct.send('GET / HTTP 1.1 \n\r\n\r'.encode())
data = cnct.recv(1024)
while data != ''.encode():
    print(str(data))
    data = cnct.recv(1024)


