"""server.py""" 

import socket
import sys

if __name__ == "__main__":

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
self.host = host()
self.host = port()
port = 9999
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket.address = serversocket.accept()

print("Connection from %s" % str(address))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()