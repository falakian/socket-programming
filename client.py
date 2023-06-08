import socket
import threading

SERVER_ADDRESS = '127.0.0.1'
PORT = 12000
socket_conn={}
connection_in=[]

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((SERVER_ADDRESS, PORT))