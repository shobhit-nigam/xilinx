import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = address family ipv4
#SOCK_STREAM = TCP protocol
#reserve a port
port = 12445
#bind to the port
s.bind(('', port))
print('socket binded to ', port)
s.listen()
print('socket is listening')

while True:
    con, addr = s.accept()
    print('recieved connection from', addr)
    data = 'thanks for connecting'
    byt = data.encode()
    con.send(byt)
    con.close()

