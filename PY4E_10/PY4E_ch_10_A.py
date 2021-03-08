# Exercise 1: Revise a previous program as follows:
# Read and parse the “From” lines
# pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
#
# After all the data has been read,
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.
#
#-----------------------------------

usr_inp = input('enter file name >>> ')
f_handl = open(usr_inp)


d = dict()
for line in f_handl:
    if line.startswith('From:') :
        # print(line)
        l_splt = line.split()
        # print(l_splt[1])
        e_addr = l_splt[1]
        uname, domain = e_addr.split('@')
        # print(domain)
        d[domain] = d.get(domain, 0) + 1


# print(d.keys())
# print(d.values())
# print(d.items())
print(sorted([(v, k) for k, v in d.items()], reverse=True))

def dct_max_fun(d) :
    max_val = 0
    max_key = None
    for key,count in d.items():
# code from PY4E discussion, by Arran Patterson
# if max is None or count > bigcount:
        if count > max_val :
            max_val = count
            max_key = key
    # print(max_key, max_val)
    print('the MOST emails, {0}, were sent by {1}'.format(max_val, max_key))

dct_max_fun()    

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### copypaste of code from PY4E_ch_8_D
