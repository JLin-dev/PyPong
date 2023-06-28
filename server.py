import socket
import keyboard # pip install keyboard

HOST = '192.168.1.15'  # The server's hostname or IP address 
PORT = 12345        # The port used for the server
buffer_size = 1024


def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections (this is use for TDP)
    # server_socket.listen()
    # Listen for incoming connections (UTP)
    print("Server listening on {}:{}".format(HOST, PORT))

    # Register the key press event handler
    keyboard.on_press(lambda event: handle_key_press(event, server_socket))

    while True:
        # Accept incoming connections
        data, client_address = server_socket.recvfrom(buffer_size)
        print("Connected to client:", client_address)
        print("Data:", data.decode())


# Function to handle key press events
def handle_key_press(event, server_socket):
    
    if event.name == 'pause':  # Press 'pause' to quit the server
        # Clean up and exit the server
        server_socket.close()
        print("Server closed.")
        exit()


if __name__ == '__main__':
    main()

