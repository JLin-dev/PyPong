import socket
import keyboard # pip install keyboard
from _thread import *
import sys

HOST = '192.168.1.15'  # The server's hostname or IP address 
PORT = 12345        # The port used for the server
buffer_size = 1024
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Bind the socket to a specific address and port
    server_socket.bind((HOST, PORT))
except socket.error as e:
    str(e)




# Listen for incoming connections (this is use for TDP)
    # server_socket.listen()
    # Listen for incoming connections (UTP)
print("Server listening on {}:{}".format(HOST, PORT))

# have mutiple clinet that may connect to 
def threaded_clinet(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recevied: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break




# continuously looking for new clinet
while True:
    conn , client_address = server_socket.recvfrom(buffer_size)
    start_new_thread(threaded_clinet, (conn, ))
    




