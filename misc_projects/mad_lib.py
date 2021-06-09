#http://data.pr4e.org/romeo.txt

#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import urllib.request
import re
#----••••••••----••••••••----••••••••----#
#usr_host = str(input('enter URL below\n>>> '))
usr_host = 'http://data.pr4e.org/romeo.txt'
usr_host = usr_host.rstrip()
#print(usr_host)
#----••••••••----••••••••----••••••••----#
with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    #print(type(html))
    #print(html)
#----••••••••----••••••••----••••••••----#
def romeo_mad_lib(t) :
    global html
#----••••••••----••••••••----••••••••----#
    for_splice = html.split()
#----••••••••----••••••••----••••••••----#
    adj = [1, 5, 18, 23, 28, 30]
    
    adj_mapping = map(for_splice.__getitem__, adj)
    adj_map_list = list(adj_mapping) 
    print('adjectives: {0}'.format(adj_map_list))
    
    new_adj = ['hard', 'fluffy', 'stinky', 'wet', 'colorful', 'crunchy']
    #new_adj = []
    while len(new_adj) < 6 :
        new_adj.append(input('Enter an ADJECTIVE below,\n>>> '))
    #print(new_adj)    
    
    adj_dict = {x:y for x,y in zip(adj_map_list, new_adj)}
    
    for a_tup in [adj_dict]:
        pattern = re.compile("|".join(a_tup.keys()))
        new_string1 = pattern.sub(lambda m: a_tup[re.escape(m.group(0))], t)  
#----••••••••----••••••••----••••••••----#
    noun = [3, 6, 11, 16, 19, 24, -1]
    
    noun_mapping = map(for_splice.__getitem__, noun)
    noun_map_list = list(noun_mapping)
    print('nouns: {0}'.format(noun_map_list))
   
    new_noun = ['cat', 'rock', 'river', 'train', 'butt', 'cheese']
    #new_adj = []
    while len(new_noun) < 6 :
        new_noun.append(input('Enter a NOUN below,\n>>> '))
    #print(new_noun)
        
    noun_dict = {x:y for x,y in zip(noun_map_list, new_noun)}
    
    for n_tup in [noun_dict]:
        pattern = re.compile("|".join(n_tup.keys()))
        new_string2 = pattern.sub(lambda m: n_tup[re.escape(m.group(0))], new_string1)
#----••••••••----••••••••----••••••••----#
    verb = [7, 17, 21]

    verb_mapping = map(for_splice.__getitem__, verb)
    verb_map_list = list(verb_mapping)
    print('verbs: {0}'.format(verb_map_list))
    
    new_verb = ['swim', 'fart', 'explode']
    #new_adj = []
    while len(new_verb) < 3 :
        new_verb.append(input('Enter a VERB below,\n>>> '))
    #print(new_verb)
        
    verb_dict = {x:y for x,y in zip(verb_map_list, new_verb)}
    
    for v_tup in [verb_dict]:
        pattern = re.compile("|".join(v_tup.keys()))
        new_string3 = pattern.sub(lambda m: v_tup[re.escape(m.group(0))], new_string2)
#----••••••••----••••••••----••••••••----#
    return new_string3
#----••••••••----••••••••----••••••••----#
print('\n{0}'.format(romeo_mad_lib(html)))
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#