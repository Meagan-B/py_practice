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

def romeo_mad_lib()
    global html
    
    for_splice = html.split()

    adj = [1, 5, 18, 23, 28, 30]
    adj_mapping = map(for_splice.__getitem__, adj)
    adj_map_list = list(adj_mapping) 
    print('adjectives: {0}'.format(adj_map_list))
    
    adj_dict = {x:y for x,y in zip(in_alpha, out_alpha)}
    #print(letter_dict1)
    
    #CODE FROM O_STACK >>>
    for a_tup in [adj_dict]:
        pattern = re.compile("|".join(w_dict.keys()))
        #print(pattern)
        my_string = pattern.sub(lambda m: w_dict[re.escape(m.group(0))], t)
        #print(my_string)
# ----
    noun = [3, 6, 16, 19, 24, -1]
    noun_mapping = map(for_splice.__getitem__, noun)
    noun_map_list = list(noun_mapping)
    print('nouns: {0}'.format(noun_map_list))
# ----
    verb = [7, 17, 21]
    verb_mapping = map(for_splice.__getitem__, verb)
    verb_map_list = list(verb_mapping)
    print('verbs: {0}'.format(verb_map_list))

# ----
    
    
    
    return my_string