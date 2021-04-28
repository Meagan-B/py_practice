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
# print(html)

# soup = BeautifulSoup(requests.get(usr_host).text, 'html.parser')
soup = BeautifulSoup(usr_host.text, 'html.parser')
# print(soup)

collection_pot = []
for story_head in soup.find_all(class_='story-wrapper css-dqoo0l') :
    collection_pot += story_head
    # print(story_head)

print(collection_pot)
# ----

# <h3 class="css-svu3ba e1lsht870" size="500">Can You Have Alcohol After the Covid Vaccine?</h3>
# <h3 class="css-1bxzzgs e1lsht870" size="300">Why Iowa Has Become Such a Heartbreaker for Democrats</h3>


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
