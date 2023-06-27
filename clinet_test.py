import socket

# Server address
server_ip = '192.168.1.15'  # Replace with the server's IP address
server_port = 12345  # Replace with the server's port number

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server

# In Python, adding the b prefix to a string creates a bytes object instead of a regular string.
data = b'Hello, server!'
sock.sendto(data, (server_ip, server_port))

# Close the socket
sock.close()

