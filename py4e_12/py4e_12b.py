# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
# >>>>>>>>>>>>>>>>>>>>>>>

import re
import socket

# ----

usr_url = str(input('enter URL below\n>>> '))
usr_url = usr_url.rstrip()

if re.search('/+', usr_url) :
    usr_url = usr_url.split('/')
    # print(usr_url)
    for i in usr_url :
        if re.search('^.+\..+\.[a-z]+$', i) :
            usr_url = i
            # print(usr_url)

print(type(usr_url), usr_url)
# ----

try :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((usr_url, 80))
    # h_proto = ('GET {0} HTTP/1.0\r\n\r\n'.format(usr_url)).encode()
    h_proto = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    sock.send(h_proto)

    while True :
        data = sock.recv(512)
        if len(data) < 1 :
            break
        # print(data.decode(), end='')
except :
    print('OOPS, bad link')



# ----


# ----

# ----

# ----

sock.close()
# ...........................
