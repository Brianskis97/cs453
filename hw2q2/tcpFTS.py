#! /usr/bin/python3

import socket
import bz2

host = '127.0.0.1'
port = 12345

flag1 = True;
flag2 = True;

print("Ctrl + C to exit\n")

cnct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnct.bind((host,port))
cnct.listen(1)
try:
	while flag1:
		print("Awaiting client connection...")
		conn, addr = cnct.accept()
		uncom = open("uncompressed", "wb")
		while True:
			print("Awaiting file...")
			data = conn.recv(1024)	
			uncom.write(data)
			if not data:
				uncom.close()
				break
		conn, addr = cnct.accept()
		print("File recieved, compressing")	
		with open('uncompressed','rb') as data:
			bz2comp = bz2.compress(data.read(), 9)
		output = open('hosts.bz2', 'wb')
		output.write(bz2comp)
		output.close()
		print("Compressed, sending to client")
		output = open('hosts.bz2', 'rb')
		outCM = output.read(1024)
		while outCM != ''.encode():
			conn.send(outCM)
			print(outCM)
			outCM = output.read(1024)
		print("Sent, closing connection to client")
		conn.close()
except (KeyboardInterrupt, SystemExit):
	print("\nBye now\n")
	cnct.close()
	quit()		
