# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1154832.xml (Sum ends with 86)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ----
# Ignore SSL certificate errors (from PY4E, because i do not understand, but need to use this code to test example)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ----

# url = input('enter URL below\n>>> ')
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# url = "http://py4e-data.dr-chuck.net/comments_1154832.xml"
# print(url)

# ----

data = urllib.request.urlopen(url, context=ctx).read().decode()
# print(type(data), data)
tree = ET.fromstring(data)
# print(type(tree), tree)

# ----

counts = tree.findall('comments/comment')
# print(type(counts), counts)

data_pnts = len(counts)

# ----

sum = 0

for i in counts :
    # print(i)
    c = i.find('count').text
    # print(c)
    c = int(c)
    sum += c

# ----

avg = (sum / data_pnts)
print(avg)

# ----

print('COUNT of data points {0}\nSUM of comments {1}\nAVERAGE comments made per person {2}'.format(data_pnts, sum, avg))

# ...........................
