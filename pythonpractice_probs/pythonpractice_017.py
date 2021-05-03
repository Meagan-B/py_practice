# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# >>>>>>>>>>>>>>>>>>>>>

import re
import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl

# ----
# Ignore SSL certificate errors (from PY4E, because i do not understand, but need to use this code to test example)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ----

# usr_host = input('enter web address below\n>>> ')
# usr_host = 'http://www.nytimes.com'
# html = requests.get(usr_host)
# soup = BeautifulSoup(requests.get(usr_host).text, 'lxml')

# ----

fhand = urllib.request.urlopen('http://www.nytimes.com')
for line in fhand:
    print(line.decode().strip())
# ----

# count = 0
# link_collect =[]

# tags = soup.find_all('a', [class_="css-xxaj7r")

# tags = soup.find_all('a')
# print(tags)
    # tags = soup.find_all("a", class_="css-xxaj7r e1lsht870")
    # tags = soup.title
    # tags = soup.title.name
    # tags = soup.title.string
    # tags = soup.title.parent.name
    # tags = soup.p

# for tag in tags :
#     if tag.re('class= css-xxaj7r') :
#         # link_collect.append(tag.get('href'))
#         link_collect.append(tag)
#         count += 1
#     else : continue

# print(link_collect)



# ...........................
