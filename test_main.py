"""Test for Http fucntion"""

import socket

def __init__(self, host, port):
    clientsocket = socket.socket()
    clientsocket.settimeout(1)
    clientsocket.connect(('localhost', 9999))
    clientsocket.bind(('127.0.0.1', 9999))
    clientsocket.listen(5)
    clientsocket.accept()
    clientsocket.close()


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def handle_client(self, client):
        client.close()
    return 

    def start_listening(self):
        serversocket = socket.socket()
        serversocket.bind((self.host, self.port))
        serversocket.listen(3)

        client.address = socket.accept()
        client_handler = threading.Thread(target=self.handle_client,args=(client,))
        client_handler.start()