#! /usr/bin/python3

import socket
import bz2

host = '127.0.0.1'
port = 12345
address = (host, port)

flag1 = True;
flag2 = True;


cnct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cnct.bind(address)
print("Ctrl + C to exit\n");
try:
	while flag1:
		uncom = open("uncom", "w+b")
		while True:
			print("Awaiting File...")	
			data, sender = cnct.recvfrom(1024)	
			if data == '~&$END$&~'.encode():
				uncom.close()
				break
			uncom.write(data)
		print("File recieved, compressing")	
		with open('uncom','rb') as data:
			bz2comp = bz2.compress(data.read(), 9)
		output = open('hosts.bz2', 'wb')
		output.write(bz2comp)
		output.close()
		print("Compressed")
		output = open('hosts.bz2', 'rb')
		outCM = output.read(1024)
		while outCM != ''.encode():
			sent = cnct.sendto(outCM, sender)
			outCM = output.read(1024)
		output.close()
		cnct.sendto('~&$END$&~'.encode(),sender)
		print("File sent\n")
except (KeyboardInterrupt, SystemExit):
	print("\nBye now\n")
	cnct.close()
	quit()
