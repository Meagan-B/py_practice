#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that
#many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
import datetime
current_date = datetime.datetime.utcnow()

#----

usrname = input('enter your name >>')
print('hello, ' + usrname.capitalize())

#----

while True:
    usrage = input('enter your age >>')
    try:
        i_usrage = int(usrage)
        break
    except:
        print('!ERROR! enter age in numbers >>')
#----

if i_usrage < 100 :
    yrscalc = 100 - i_usrage
    mscalc = yrscalc * 12
    wkscalc = yrscalc * 52
    dyscalc = 365 *  yrscalc
    num_dysto100 = current_date + datetime.timedelta(days = dyscalc)
else :
    print('you WIN @ life!  ' * 100 )

#----

print('%s will turn 100 in the year ~ %s ~' % (usrname.capitalize(), num_dysto100.year))
print('%s years to 100' % yrscalc)
print('%s months to 100' % mscalc)
print('%s weeks to 100' % wkscalc)
print('%s days to 100' % dyscalc)

#----

fin = input('enter Q to exit program >>')
if fin == 'Q' or 'q' :
    print(('thank you for playing!' + '\n') * 100 )
    exit()
#.......................... 
