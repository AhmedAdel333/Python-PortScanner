import socket
from socket import AF_INET, SOCK_STREAM
import threading 
from threading import Thread

banner = """
		 ____  ____  _____/ /_   ______________ _____  ____  ___  _____
   / __ \/ __ \/ ___/ __/  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
  / /_/ / /_/ / /  / /_   (__  ) /__/ /_/ / / / / / / /  __/ /    
 / .___/\____/_/   \__/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/  v 0.9
 															coded by </Win32>   
"""

print (banner)
tgt = input ("target: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))
port_list = range(start_port, end_port)

def port_scan(tgt):
	for port in port_list:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.settimeout(2)
		try:
			conn.connect((tgt, port))
			while True:
				print ("[+] port ", port, "is open")
				break;
		except socket.error:
			print ("[-] port ", port, "is closed")


th = threading.Thread(target=port_scan(tgt))
th.daemon = True
th.start()