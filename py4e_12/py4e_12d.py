# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# 
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
#
# # Code: http://www.py4e.com/code3/urllinks.py
# >>>>>>>>>>>>>>>>>>>>>>>

import re
import urllib.request
from gtts import gTTS
import os

# ----

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

# ----

with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    if

    # doc_len = re.sub(r' ', '', html)
    # doc_len = re.sub(r'\n', '', doc_len)
    # doc_len = re.sub(r'\r', '', doc_len)
    # doc_len = len(doc_len)

    # print('\n')
    # print(html[:3000])
    # print('\n**** {0} characters found ****\n'.format(doc_len))

# ----

language = 'en'

audio_read = gTTS(text=html, lang=language, slow=False)
audio_read.save("but_soft.mp3")

# ----

os.system("afplay but_soft.mp3")
# ----

# ----

# ----

# ----

# ...........................
