# UDP Server

import socket
import uuid
import time
import datetime

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((host, port))

    while True:
        data, address = server.recvfrom(1024)
        data = data.decode("utf-8")
        
        if data == "end":
            print("Client Disconnected")
            break

        print(data)
        print("Connection Protocol:  UDP")
        print("Source MAC address:  ", hex(uuid.getnode()))
        print("IP address:  ", host)
        print("Port number:  ", port)
        print("Date and time:  " + str(datetime.datetime.now()))

    
        data = data.upper()
        data = data.encode("utf-8")
        server.sendto(data, address)


host = socket.gethostname()
