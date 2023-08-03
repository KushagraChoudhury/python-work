import socket

host='localhost'
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

# receive message from server at a time 1024 bytes
msg=s.recv(1024)

while msg:
    print('Received '+msg.decode())
    msg=s.recv(1024)

s.close()