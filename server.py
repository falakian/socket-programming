import socket
import threading
def handle_user_connection(connection: socket.socket, address: tuple):
     while True:
            msg = connection.recv(2048)
            if msg :
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