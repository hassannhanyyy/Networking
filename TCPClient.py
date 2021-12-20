# TCP Client

import socket

message = ""

host = socket.gethostname()

port_number = 3030

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    s.connect((host,port_number))
    
    name = input("* What's your name? ")
    
    welcome = input("* Hello " + name.capitalize() + "(Write 'end' to disconnect)\n* ")

    while (message.lower().strip() == "end"):
    
        message = input("* ")

print("* Disconnected")
