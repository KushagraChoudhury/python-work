import socket as ss

host='localhost'
port=5000

# create a socket at server side using TCP/IP

s=ss.socket(ss.AF_INET,ss.SOCK_STREAM)
# s=ss.socket()

# bind the socket to my settings

s.bind((host,port))

s.listen(1)

c,add=s.accept()
print('A client connected')

while True:
    data=c.recv(1024)
    if not data:
        break
    print('From Client:  ',str(data.decode()))

    data1=input('enter response : ')
    c.send(data1.encode())

c.close()

