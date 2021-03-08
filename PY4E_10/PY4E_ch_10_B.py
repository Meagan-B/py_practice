# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by;
# finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour,
# print out the counts,
# one per line,
# sorted by hour as shown below.
# #
# -------------------------------

usr_inp = input('enter file name >>> ')
f_handl = open(usr_inp)


d = dict()
for line in f_handl:
    if line.startswith('From ') :
        print(line)
        l_splt = line.split()
        # print(l_splt[1])
        # e_addr = l_splt[1]
        hrs = l_splt[5]
        time_brk = hrs.split(':')
        hrs_ext = time_brk[0]
        print(hrs_ext)
        # d[domain] = d.get(domain, 0) + 1
        # d[uname] = d.get(uname, 0) + 1
        d[hrs_ext] = d.get(hrs_ext, 0) + 1

# print(d.keys())
# print(d.values())
# print(d.items())
hrs_srtd = sorted([(k, v) for k, v in d.items()], reverse=True)
print(hrs_srtd)

# def dct_max_fun(d) :
#     max_val = 0
#     max_key = None
#     for key,count in d.items():
# # code from PY4E discussion, by Arran Patterson
# # if max is None or count > bigcount:
#         if count > max_val :
#             max_val = count
#             max_key = key
#     # print(max_key, max_val)
#     # print('the MOST emails, {0}, were sent by {1}'.format(max_val, max_key))
#
# dct_max_fun(d)

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### copypaste of code from PY4E_ch_9_E
