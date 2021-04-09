# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
# >>>>>>>>>>>>>>>>>>>>>>>


# ----

# ----

# ----

# ----

# ...........................
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

# ----
data_collect = str()

try :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((usr_host, 80))
    # h_proto = ('GET {0} HTTP/1.0\r\n\r\n'.format(usr_host)).encode()
    h_proto = 'GET http://data.pr4e.org/ HTTP/1.0\r\n\r\n'.encode()
    sock.send(h_proto)
except :
    print('OOPS, bad link')

# ----

data_str = 'data_str\n'

while True :
    data = sock.recv(512)
    data_str.append(data)
    if len(data) < 1 :
        # data_str = data.decode()
        print(data_str)
        # data_no_hed = re.split('(\r\n\r\n)?', data_str)
        # print(data_no_hed)
        break
# ----

# print(data)
# print(data.decode())
# print('\n••••••••••\n')
# data = re.split('(\r\n\r\n)?', data)

# ----

sock.close()

# ...........................
