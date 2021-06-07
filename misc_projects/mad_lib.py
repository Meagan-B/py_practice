#http://data.pr4e.org/romeo.txt

# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request

# ----

usr_host = str(input('enter URL below\n>>> '))
print(usr_host)
usr_host = usr_host.rstrip()
print(usr_host)

# ----

with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    # print(type(html))