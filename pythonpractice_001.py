#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that
#many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)
import datetime
current_date = datetime.datetime.utcnow()

usrname = input('enter your name >>')
print('hello, ' + usrname)


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
    #dateto100 =
    yrsto100 = 'years to 100: '
    msto100 =  'months to 100: '
    wksto100 = 'weeks to 100: '
    dysto100 = 'days to 100: '
    num_dysto100 = current_date + datetime.timedelta(days = dyscalc)
    print('year you turn 100 : %s' % num_dysto100.year)
    print(dir(num_dysto100))
    #print(dateto100)
    print(yrsto100, yrscalc)
    #print(msto100, mscalc)
    #print(wksto100, wkscalc)
    #print(dysto100, dyscalc)
else :
    print('you WIN @ life!  ' * 100 )

print('thank you for playing!')
