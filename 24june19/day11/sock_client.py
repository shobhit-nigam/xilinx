import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = address family ipv4
#SOCK_STREAM = TCP protocol
#reserve a port
port = 12445
#bind to the port
s.connect(('127.0.0.1', port))

data = s.recv(2000)
obj = data.decode()
print(obj)
s.close()
