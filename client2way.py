import socket as ss

host='localhost'
port=5000

# create a socket at server side using TCP/IP

# s=ss.socket(ss.AF_INET,ss.SOCK_STREAM)
s=ss.socket()

# bind the socket to my settings

s.connect((host,port))

str=input('Enter data: ')

# continue as long as client types exit

while str!='exit':
    s.send(str.encode())

    data=s.recv(1024)
    data=data.decode()
    print('message from server ',data)
    str=input('enter data ')

s.close()