"""client.py"""

import socket
import sys

if __name__ == "__main__":

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 9999))
data = socket.recv(1024)
result = "recieved some data"
clientsocket.sendall(data)
print result
    clientsock.close()
except Keyboarinterrupt:
    print("shutting down server.")
    break
