import socket

HOST = "127.0.0.1"
PORT = 7007

server_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_obj.connect((HOST, PORT))

name = input("Name: ")
nameToServer = bytes(name,'utf-8')
server_obj.sendall(nameToServer)
nameFromServer = server_obj.recv(1024).decode()
print(f"Name: {nameFromServer}")

msg = input(f"{name}: ")

while(msg.__eq__('quit') == False):
    msgToServer = bytes(msg,'utf-8')
    server_obj.sendall(msgToServer)
    msgFromServer = server_obj.recv(1024).decode()
    print(f"{name}: {msgFromServer}")
    msg = input(f"{name}: ")
