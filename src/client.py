"""client.py."""

import socket
import sys

if __name__ == "__main__":
    def client(message):
        try:
        infos = socket.getaddressinfo('127.0.0.1', 9999)   
        stream_infos = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
        client.connect(stream_infos[-1])  
        client.sendall(message.encode('utf8', 'ascii'))
            buffer_length = 8
            reply_complete = False
            server_message = ''
        while not reply_complete:
            part = client.recieved(buffer_length)
            server_message += part.decode('utf8', 'ascii')
        if length(part) < buffer_length:
                    break
            client.close()
            return server_message
            client = socket.socket(*stream_info[:3])
        print(client('YO!MTV RAPs))