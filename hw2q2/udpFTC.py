#! /usr/bin/python3

import socket

inFile = open("/etc/hosts", 'rb')

ip = '127.0.0.1'
port = 12345
address = (ip, port)
cnct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


outData = inFile.read(1024)
while outData != ''.encode():
	sent = cnct.sendto(outData, address)
	outData = inFile.read(1024)
sent = cnct.sendto('~&$END$&~'.encode(), address)
recvCMP = open('recvCMP', 'w+b')
while True:
	data, sender = cnct.recvfrom(1024)
	if data == '~&$END$&~'.encode():
		recvCMP.close()
		cnct.close()
		break
	else:
		recvCMP.write(data)
