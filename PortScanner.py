import socket
from socket import AF_INET, SOCK_STREAM
import sys


tgt = sys.argv[2]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
port_list = range(start_port, end_port)

def port_scan(tgt, port_list):
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


port_scan(tgt, port_list)
