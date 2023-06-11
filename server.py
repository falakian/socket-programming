import socket
import threading
import struct
import random
def handle_user_connection(connection: socket.socket, address: tuple):
     while True:
            msg = connection.recv(2048)
            if msg :
                typ,strcode,message_recv = struct.unpack('b 15s 2000s',msg)
                message_recv=message_recv.decode('utf-8')
                message_recv=message_recv.replace("\0", "")
                strcode=strcode.decode('utf-8')
                strcode=strcode.replace("\0", "")
                if typ ==1:
                    print("{} : It requested the list of active clients from the server".format(strcode))
                    print(" ")
                    packing=str(len(active_connections))+" _ "
                    packing+=" _ ".join(active_connections.keys())
                    packet = struct.pack('b 15s 2000s ', 10 ,bytes("Server", 'utf-8'), bytes(packing, 'utf-8'))
                    connection.send(packet)
                    print("{} : The server sent a list of active clients".format(strcode))
                    print(" ")
                elif typ == 2:
                    if message_recv == "active":
                        print("{} : Request to the server to activate".format(strcode))
                        print(" ")
                        if strcode in active_connections.keys():
                            packet = struct.pack('b 15s 2000s', 12 ,bytes("Server", 'utf-8'),bytes("You were already in the list of active clients", 'utf-8'))
                            connection.send(packet)
                            print("{} : It has been active before".format(strcode))
                            print(" ")
                        else:
                            active_connections[strcode]=address
                            packet = struct.pack('b 15s 2000s', 12 ,bytes("Server", 'utf-8'),bytes("Success _ You are activated", 'utf-8'))
                            connection.send(packet)
                            print("{} : Activated successfully".format(strcode))
                            print(" ")
                    elif message_recv == "inactivate":
                        print("{} : Request to server to inactive".format(strcode))
                        print(" ")
                        if strcode in active_connections.keys():
                            del active_connections[strcode]
                            packet = struct.pack('b 15s 2000s', 12 ,bytes("Server", 'utf-8'),bytes("Success _ You have been deactivated", 'utf-8'))
                            connection.send(packet)
                            print("{} : Deactivated successfully".format(strcode))
                            print(" ")
                        else:
                            packet = struct.pack('b 15s 2000s', 12 ,bytes("Server", 'utf-8'),bytes("You are not active to become inactive", 'utf-8'))
                            connection.send(packet)
                            print("{} : It has been inactive".format(strcode))
                            print(" ")
                    else :
                        print("{} : This request is unknown to the server".format(strcode))
                        print(" ")
                        packet = struct.pack('b 15s 2000s', 12 ,bytes("Server", 'utf-8'),bytes("The command was wrong", 'utf-8'))
                        connection.send(packet)
                elif typ == 3:
                        if strcode in connections.keys():
                            packet = struct.pack('b 15s 2000s', 3 ,bytes("Server", 'utf-8'),bytes("Failed", 'utf-8'))
                            connection.send(packet)
                        else:
                            while True:
                                ip_address="127"
                                ran1=random.randrange(0,255)
                                ran2=random.randrange(0,255)
                                ran3=random.randrange(2,254)
                                ip_address+="."+str(ran1)+"."+str(ran2)+"."+str(ran3)
                                if(ip_address in ip_add):
                                    continue
                                else:
                                    connections[strcode]=ip_address
                                    packet = struct.pack('b 15s 2000s', 3 ,bytes("Server", 'utf-8'),bytes(ip_address, 'utf-8'))
                                    connection.send(packet)
                                    print("{} : The client is connected to the server".format(strcode))
                                    print("{}'s IP is {}".format(strcode,ip_address))
                                    print(" ")
                                    break
                elif typ == 4:
                     pass
                else:
                     pass
            
            else:
                    connection.close()
  
listening_port = 12000
connections = {}
active_connections = {}
ip_add=[]

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('127.0.0.1', listening_port))
socket_server.listen()

while True:
    socket_connection, address_c = socket_server.accept()
    
    threading.Thread(target=handle_user_connection, args=[socket_connection, address_c]).start()