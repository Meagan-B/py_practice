# Exercise 3: Use urllib to replicate the previous exercise of
#
# (1) retrieving the document from a URL,
#
# (2) displaying up to 3000 characters, and
#
# (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
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
    doc_len = len(html)
    print(html[:3000].decode())
    print('\n{0} characters found'.format(doc_len))

# ----

    # links = re.findall(b'href="(.*?\..*?)"', html)
    # for link in links :
    #     print(link.decode())
    #
    # link_pik = input('\r\n\r\nenter a link, from list above\n>>> ').urlopen(link_pik)

    # print(html)

# ----

# ----

# ----

# ...........................
