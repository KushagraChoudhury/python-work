import socket as s
# host="www.google.co.in"

try:
    adr=s.gethostbyname(input('enter input :'))
    print('IP address '+adr)

except:
    print('ERROR')

print('------------------------------')