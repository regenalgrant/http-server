""" Test for Http function"""

import socket
import sys

class client(object):

    def __int__(self, host, port):
       from client import socket
        clientsocket = socket.socket()
        clientsocket.timeout(1)
        clientsocket.connect(('127.0.0.1', 9999))
        clientsocket.bind((host, port))
        clientsocket.listen(5)
        clientsocket.accept()
        clientsocket.close()


class server(object):

    def __init__(self, host, port):
        from server import socket
        self.host = host
        self.port = port

    def handle_client(self, client):
        pass
        client.close()
    return 

    def start_listening(self):
        pass
        serversocket = socket.socket()
        serversocket.bind((self.host, self.port))
        serversocket.listen(3)

        client, address = socket.accept()
        client_handler = threading.Thread(target=self.handle_client,args=(client,))
        client_handler.start()