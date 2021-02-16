#Exercise 6: Read the documentation of the string methods at
#https://docs.python.org/library/stdtypes.html
#You might want to experiment with some of them to make sure you understand how they work.
#strip and replace are particularly useful.
#The documentation uses a syntax that might be confusing.
#For example, in find(sub[, start[, end]]), the brackets indicate optional arguments.
#So sub is required, but start is optional, and if you include start, then end is optional.

#rework of previous program to look for implementations of, str.capitalize(), str.join(iterable), s[i] = x
#pythonpractice_001.py, time and date to 100

import datetime
current_date = datetime.datetime.utcnow()

usrname = input('enter your name >>')
#str.capitalize()
print('hello, ' + usrname.capitalize())

while True:
    usrage = input('enter your age >>')
    try:
        i_usrage = int(usrage)
        break
    except:
        print('!ERROR! enter age in numbers >>')

if i_usrage < 100 :
    yrscalc = 100 - i_usrage
    mscalc = yrscalc * 12
    wkscalc = yrscalc * 52
    dyscalc = 365 *  yrscalc
    num_dysto100 = current_date + datetime.timedelta(days = dyscalc)
else :
    print('you WIN @ life!  ' * 100 )

print('%s will turn 100 in the year ~ %s ~' % (usrname.capitalize(), num_dysto100.year))
print('%s years to 100' % yrscalc)
print('%s months to 100' % mscalc)
print('%s weeks to 100' % wkscalc)
print('%s days to 100' % dyscalc)

#TRIED s[i] = x, but couldn't get it to work
#DID NOT find a place to use str.join(iterable)

print('thank you for playing!')
