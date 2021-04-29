# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# >>>>>>>>>>>>>>>>>>>>>

import re
import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup

# usr_host = input('enter web address below\n>>> ')
usr_host = 'http://www.nytimes.com'
html = requests.get(usr_host)
soup = BeautifulSoup(requests.get(usr_host).text, 'lxml')

# ----

count = 0
link_collect =[]

# tags = soup.find_all('a', [class_="css-xxaj7r")

while count < 4 :
    tags = soup.find_all('a')
    # tags = soup.find_all("a", class_="css-xxaj7r e1lsht870")
    # tags = soup.title
    # tags = soup.title.name
    # tags = soup.title.string
    # tags = soup.title.parent.name
    # tags = soup.p
    for tag in tags :
        if tag.re('class= css-xxaj7r') :
            # link_collect.append(tag.get('href'))
            link_collect.append(tag)
            count += 1
        else : continue

print(link_collect)
    # ----

    # i = input('\nenter position\n>>> ')
    # i = int(i) - 1
    #
    #
    # next_link = link_collect[i]
    # print('\nnext link to follow…\n{0}\n'.format(next_link))
    # # usr_host = tag_collect[2]
    # # print(usr_host)
    # count += 1
    #
    # # ----
    #
    # cont = input('want to follow another link?\nY for yes, N for no\n>>> ')
    #
    # if cont == 'Y' or cont == 'y' : continue
    # elif cont == 'N' or cont == 'n'  : break




# # ----
#
# # usr_host = str(input('enter URL below\n>>> '))
# # usr_host = usr_host.rstrip()
# usr_host = 'http://www.nytimes.com'
#
# # ----
#
# html = requests.get(usr_host)
# # print(html.decode())
# # print(html)
#
# soup = BeautifulSoup(requests.get(usr_host).text, 'html.parser')
# # soup = BeautifulSoup(usr_host.text, 'html.parser')
# # print(soup)
#
# collection_pot = []
# for story_head in soup.find_all(class_='balancedHeadline') :
#     collection_pot += story_head
#     # print(story_head)
#
# print(collection_pot)
# # ----
#
# # <h3 class="css-svu3ba e1lsht870" size="500">Can You Have Alcohol After the Covid Vaccine?</h3>
# # <h3 class="css-1bxzzgs e1lsht870" size="300">Why Iowa Has Become Such a Heartbreaker for Democrats</h3>
#
#
# # para_count = 0
# # para_tag = soup('p')
# #
# # for tag in para_tag :
# #     para_count += 1
# #
# # # ----
# #
# # print('\n**** {0} paragraphs found ****\n'.format(para_count))




# ...........................
