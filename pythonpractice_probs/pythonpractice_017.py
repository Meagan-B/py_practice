# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# >>>>>>>>>>>>>>>>>>>>>


import requests
from bs4 import BeautifulSoup

# ----

# usr_host = str(input('enter URL below\n>>> '))
# usr_host = usr_host.rstrip()
usr_host = 'http://www.nytimes.com'

# ----

html = requests.get(usr_host)
# print(html.decode())
print(html)

soup = BeautifulSoup(html.text)
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
