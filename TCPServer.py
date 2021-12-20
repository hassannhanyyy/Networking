# TCP Server

import socket
import uuid
import time
import datetime

host = socket.gethostname() 

port_number = 3030

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port_number))
    s.listen()
    
    connect,address = s.accept()

    with connect:

        print("Connection Protocol:  TCP")
        print("Source MAC address:  ", hex(uuid.getnode()))
        print("Connected by  ", address)
        print("Date and time:  " + str(datetime.datetime.now()))
        
        while True:

            data = connect.recv(1024)
            
            if not data:
    
                break

            connect.sendall(data)
