# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# >>>>>>>>>>>>>>>>>>>>>

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

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

# ----

html = urllib.request.urlopen(usr_host, context=ctx).read()
# print(html.decode())

soup = BeautifulSoup(html, 'html.parser')
print(soup)

# ----

# para_count = 0
# para_tag = soup('p')
#
# for tag in para_tag :
#     para_count += 1
#
# # ----
#
# print('\n**** {0} paragraphs found ****\n'.format(para_count))





# ...........................
