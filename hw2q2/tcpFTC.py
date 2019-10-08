#! /usr/bin/python3

import socket

inFile = open("/etc/hosts", 'rb')

ip = '127.0.0.1'
port = 12345
cnct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnct.connect((ip, port))

outData = inFile.read(10)
while outData != ''.encode():
	cnct.sendall(outData)
	outData = inFile.read(10)
cnct.close()
cnct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnct.connect((ip, port))
recvCMP = open('recieved.bz2', 'wb')
while True:
	data = cnct.recv(1024)
	if data == ''.encode(): 
		recvCMP.close()
		cnct.close()
		break
	else:
		recvCMP.write(data)

