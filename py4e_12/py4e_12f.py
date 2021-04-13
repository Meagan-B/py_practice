# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to
#
# http://www.py4e.com/code3/urllink2.py.
#
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1154830.html (Sum ends with 77)
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

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

# ----

html = urllib.request.urlopen(usr_host, context=ctx).read()
# print(html.decode())
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# ----

num_count = 0
nums_2_sum = []

for tag in soup.find_all('span') :
    span_tag = tag.decode()
    # print(span_tag)
    # print(type(span_tag))
    num = re.findall('\d+', span_tag)
    # print(num)
    for n in num :
        num_i = int(n)
        nums_2_sum.append(num_i)
        num_count += 1


print(nums_2_sum)
print(num_count)
# print(sum(num))


# for tag in soup.find_all(re.compile('^t')) :
#
# print('URL:',tag.get('href', None))
# print('Contents:',tag.contents[0])
# print('Attrs:',tag.attrs)
# ^PY4E

# ----


# ...........................
