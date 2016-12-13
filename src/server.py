"""server.py"""

import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.address(('127.0.0.1', 9999))
server.listen(5)
connection, address = server.accept()
message = ''
while True:
while True:
            buffer_length = 8
            message_complete = False
            while not message_complete:
                part = connection.recv(buffer_length """BUFFER_SIZE""")
                message += part.decode('utf8', 'ascii')
                if len(part) < buffer_length:
                    break
    connection.sendall(message.encode('utf8', 'ascii'))
    print(message)
    connection.close()
    server.close()  
    server()

    
    

