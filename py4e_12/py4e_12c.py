# Exercise 3: Use urllib to replicate the previous exercise of
#
# (1) retrieving the document from a URL,
#
# (2) displaying up to 3000 characters, and
#
# (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
#
# http://data.pr4e.org/romeo.txt
# >>>>>>>>>>>>>>>>>>>>>>>
import re
import urllib.request
# import time

# ----

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

# ----

with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    # print(type(html))
    doc_len = re.sub(r' ', '', html)
    doc_len = re.sub(r'\n', '', doc_len)
    doc_len = re.sub(r'\r', '', doc_len)
    doc_len = len(doc_len)
    # print(doc_len)
    print('\n')
    print(html[:3000])
    print('\n**** {0} characters found ****\n'.format(doc_len))

# ----

#print(len('ButsoftwhatlightthroughyonderwindowbreaksItistheeastandJulietisthesunArisefairsunandkilltheenviousmoonWhoisalreadysickandpalewithgrief'))

# ...........................
