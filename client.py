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

while True:
        if(flag_in==0):
            print(" ")
            print("Choose one of the options:")
            print("1) Getting a list of active clients")
            print("2) Connect to one of the clients")
            print("3) Send the command to the client")
            print("4) Close the connection with the client")
            print("5) Activation of the client in the network")
            print("6) Deactivation of the client on the network")
            print("7) Show the clients that I am connected to")
            print("8) Disconnected from the server")
            print("9) Refresh the page")
            print("10)My username and IP")
            print(" ")
            try:
                x=int(input())
                print(" ")
            except:
                x=0
            if x==1:
                packet = struct.pack('b 15s 2000s', 1 ,bytes(name, 'utf-8'),bytes(" ", 'utf-8'))
                socket_client.send(packet)
            elif x==5:
                packet = struct.pack('b 15s 2000s', 2 ,bytes(name, 'utf-8'),bytes("active", 'utf-8'))
                socket_client.send(packet)
            elif x==6:
                packet = struct.pack('b 15s 2000s', 2 ,bytes(name, 'utf-8'),bytes("inactivate", 'utf-8'))
                socket_client.send(packet)
            elif x==2:
                print("Enter the username of one of the active clients:")
                print(" ")
                user_connect=input()
                print(" ")
                if(user_connect in socket_conn.keys()):
                    print("You are connected to the client with username {}".format(user_connect))
                    print(" ")
                else:
                    packet = struct.pack('b 15s 2000s', 4 ,bytes(name, 'utf-8'),bytes(user_connect, 'utf-8'))
                    socket_client.send(packet)
                    print("Your request to connect to {} has been sent to the server".format(user_connect))
                    print(" ")
            elif x==3: 
                print("Enter the username you want to send the command to:")
                print(" ")
                user_command=input()
                print(" ")
                if(user_command in socket_conn.keys()):
                    print("Enter the command you want to send:")
                    print(" ")
                    command=input()
                    print(" ")
                    print("Command {} was sent to client {}".format(command,user_command))
                    print(" ")
                    command+=" /// "+str(len(command))
                    packet = struct.pack('b 15s 2000s', 9 ,bytes(name, 'utf-8'),bytes(command, 'utf-8'))
                    socket_conn[user_command].send(packet)
                else:
                    print("You are not connected to client {}".format(user_command))
                    print(" ")
            elif x==4:
                print("Enter the username of the client you want to disconnect:")
                print(" ")
                user_close=input()
                print(" ")
                if(user_close in socket_conn.keys()):
                    socket_conn[user_close].close()
                    del socket_conn[user_close]
                    print("You have been disconnected from client {}".format(user_close))
                    print(" ")
                else:
                    print("You are not connected to client {}".format(user_close))
                    print(" ")
            elif x==7:
                j=1
                for key in socket_conn:
                    print("{}){}".format(j,key))
                    j+=1
                print(" ")
            elif x==8:
                socket_client.close()
                raise Exception()
            elif x==9:
                continue
            elif x==10:
                print("My Username : {}".format(name))
                print("My IP : {}".format(ip_client))
                print(" ")
            else:
                print("The command was wrong")
                print(" ")
        else:
            data = connection_in[0].recv(2048)
            if data:
                typ1,strcode1,message_recv1 = struct.unpack('b 15s 2000s',data)
                username_in=strcode1.decode('utf-8')
                username_in=username_in.replace("\0", "")
                message_recv1=message_recv1.decode('utf-8')
                while True:
                    print("A client with username {} wants to connect to you, do you allow it?(Y=yes , N=no)".format(username_in))
                    print(" ")
                    flag=input()
                    print(" ")
                    if flag == 'Y' or flag == 'y':
                        socket_conn[username_in]=connection_in[0]
                        packet = struct.pack('b 15s 2000s', 12 ,bytes(name, 'utf-8'),bytes("Success _ You have successfully connected to client {}".format(name), 'utf-8'))
                        connection_in[0].send(packet)
                        print("You have successfully connected to client {}".format(username_in))
                        print(" ")
                        pass #handel_recv
                        connection_in.remove(connection_in[0])
                        break
                    elif flag == 'N' or flag == 'n':
                        packet = struct.pack('b 15s 2000s', 12 ,bytes(name, 'utf-8'),bytes("It did not allow you to connect", 'utf-8'))
                        connection_in[0].send(packet)
                        connection_in[0].close()
                        print("You are not connected to client {}".format(username_in))
                        print(" ")
                        connection_in.remove(connection_in[0])
                        break
                    else:
                        print("The command was wrong")
                        print(" ")
            else:
                connection_in[0].close()
