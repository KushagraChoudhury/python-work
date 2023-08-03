import socket as ss



host='localhost'
port=5000

# create a socket at server side using TCP/IP

s=ss.socket(ss.AF_INET,ss.SOCK_STREAM)
# s=ss.socket()

# bind the socket to my settings

s.bind((host,port))

# allow maximum 1 connection to the socket

s.listen(1)

# wait until a client accepts the connection

c,addr=s.accept()

# display the client address

print('Connection from ',str(addr))

# send message to the client after encoding the message in binary

c.send(b"Hello Client kemon achen?????")

msg="BYE"

c.send(msg.encode())

c.close()