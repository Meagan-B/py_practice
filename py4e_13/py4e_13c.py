# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.
# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request
import json
import ssl
import time

# ----

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_1154833.json'
url = input('enter URL below\n>>> ')

# ----

# Ignore SSL certificate errors (from PY4E, because i do not understand, but need to use this code to test example)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ----

response = urllib.request.urlopen(url, context=ctx)

data = json.loads(response.read())
# print(data)
# print(type(data))

# ----

# print('GATHERING, {0}'.format(url))
print('GATHERING')
time.sleep(.5)
print('......')
time.sleep(1)
print('...')
time.sleep(1)

# ----

counts = 0
sum = 0

for i in data['comments'] :
    # count += 1
    # print(i, type(i))
    c = int((i["count"]))
    counts += 1
    sum += c

# ----

print('number of users : {0}\nsum of all comments made: {1}'.format(counts, sum))

# ...........................
