# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
#
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
# Code: http://www.py4e.com/code3/socket1.py
#
# >>>>>>>>>>>>>>>>>>>>>>>

import re
import socket

# ----

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

if re.search('/+', usr_host) :
    usr_host = usr_host.split('/')
    # print(usr_url)
    for i in usr_host :
        if re.search('^.+\..+\.[a-z]+$', i) :
            usr_host = i
            # print(usr_url)

# print(type(usr_host), usr_host)
# ----
data_collect = str()

try :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((usr_host, 80))
    # h_proto = ('GET {0} HTTP/1.0\r\n\r\n'.format(usr_host)).encode()
    # h_proto = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    h_proto = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    sock.send(h_proto)

    while True :
        data = sock.recv(512)
        # print(data)
        if len(data) < 1 :
            break
        print(data.decode())
        # data_collect = data_collect.write(data.decode())

except :
    print('OOPS, bad link')


# links = re.findall(b'href="(http[s]?://.*?)"', u_fhand)
# for link in links :
#     print(links.decode())

# ----

sock.close()

# ...........................
