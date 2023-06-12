import socket
import threading
import struct
def receive():
    socket_p2p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_p2p.bind((ip_client, PORT))
    socket_p2p.listen()
    while True:
        socket_connection, address_c = socket_p2p.accept()
        connection_in.append(socket_connection)

        
SERVER_ADDRESS = '127.0.0.1'
PORT = 12000
socket_conn={}
print("Enter your username:")
name=input()
print(" ")
message_send=" "
connection_in=[]
flag_in=0
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((SERVER_ADDRESS, PORT))
packet = struct.pack('b 15s 2000s', 3 ,bytes(name, 'utf-8'),bytes(" ", 'utf-8'))
socket_client.send(packet)
while True:
        ip_data=socket_client.recv(2048)
        if(ip_data):
            ip_typ,ip_sender,ip_client=struct.unpack('b 15s 2000s',ip_data)
            ip_client=ip_client.decode('utf-8')
            ip_client = ip_client.replace("\0", "")
            if(ip_client == "Failed"):
                print("There is another client with the same username")
                print(" ")
                print("Please enter another name:")
                print(" ")
                name=input()
                print(" ")
                packet = struct.pack('b 15s 2000s', 3 ,bytes(name, 'utf-8'),bytes(" ", 'utf-8'))
                socket_client.send(packet)
            else:
                print("You have successfully connected to the server")
                print(" ")
                break

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((SERVER_ADDRESS, PORT))