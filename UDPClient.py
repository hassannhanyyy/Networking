# UDP Client

import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    address = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("* Input (Write 'end' to disconnect) \n* ")


        if data == "end":
            data = data.encode("utf-8")
            client.sendto(data, address)

            print("* Disconneted")

            break

        data = data.encode("utf-8")
        client.sendto(data, address)

        data, address = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"* Output: {data}")
