# Following Links in Python
#
# The program will use urllib to read the HTML from the data files below,
#
# extract the href= vaues from the anchor tags,
#
# scan for a tag that is in a particular position relative to the first name in the list,
#
# follow that link and repeat the process a number of times and report the last name you find.
#
#
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
#
#
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Zainib.html
#
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#
# Hint: The first character of the name of the last page that you will load is: D Strategy
#
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
#
# >>>>>>>>>>>>>>>>>>>>>>>

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ----
# Ignore SSL certificate errors (from PY4E, because i do not understand, but need to use this code to test example)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ----


count = 0

while True :
    link_collect = []

    if count < 1 :
        usr_host = str(input('enter URL below\n>>> '))
        usr_host = usr_host.rstrip()
    elif count >=1 :
        usr_host = next_link
        link_collect.clear()

    # ----

    html = urllib.request.urlopen(usr_host, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # ----

    tags = soup('a')
    for tag in tags :
        # tag_collect.append(tag)
        # print(tag.get('href', None))
        link_collect.append(tag.get('href', None))

    # ----
    i = input('\nenter position\n>>> ')
    i = int(i) - 1


    next_link = link_collect[i]
    print('\nnext link to follow…\n{0}\n'.format(next_link))
    # usr_host = tag_collect[2]
    # print(usr_host)
    count += 1

    # ----

    cont = input('want to follow another link?\nY for yes, N for no\n>>> ')

    if cont == 'Y' or cont == 'y' : continue
    elif cont == 'N' or cont == 'n'  : break

# ...........................
