import socket

HOST = '192.168.1.15'  # The server's hostname or IP address 
PORT = 12345        # The port used for the server
buffer_size = 1024

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (this is use for TDP)

# Listen for incoming connections (UTP)
# server_socket.listen()
print("Server listening on {}:{}".format(HOST, PORT))
while True:
    # Accept incoming connections
    data, client_address = server_socket.recvfrom(buffer_size)
    print("Connected to client:", client_address)
    print("Data:", data.decode())

# Close the server socket
server_socket.close()