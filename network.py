import socket


buffer_size = 1024
class Network:
    def __init__(self):
        self.clinet = socket.socket(socket.IF_INET, socket.SOCK_DGRAM)
        self.server = '192.168.1.15'
        self.port = 12345
        self.addr = (self.server, self.port)
        self.connect()
    
    def connect(self):
        try:
            
            self.clinet.connect(self.addr)
            return self.clinet.recv(buffer_size)
        except:
            pass

