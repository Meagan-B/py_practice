#http://data.pr4e.org/romeo.txt

# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request

# ----

#usr_host = str(input('enter URL below\n>>> '))
usr_host = 'http://data.pr4e.org/romeo.txt'
usr_host = usr_host.rstrip()
#print(usr_host)

# ----

with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    #print(type(html))
    #print(html)
    
# ----

for_splice = html.split()
#print(type(for_splice))
#print(for_splice)


adj = [1, 5, 11, 18, 23, 28, 30]
adj_mapping = map(for_splice.__getitem__, adj)
adj_map_list = list(adj_mapping)
print(adj_map_list)

noun = [3, 6, 16, 19, 24, -1]
noun_mapping = map(for_splice.__getitem__, noun)
noun_map_list = list(noun_mapping)
print(noun_map_list)

verb = [7, 17, 21]
verb_mapping = map(for_splice.__getitem__, verb)
verb_map_list = list(verb_mapping)
print(verb_map_list)
