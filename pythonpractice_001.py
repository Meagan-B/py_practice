#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that
#many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)
hello = 'hello,'
inpname = input('enter your name >>')
usrname = str(inpname)
print(hello.append(usrname))

usrage = input('enter your age >>')
while True:
    try:
        i_usrage = int(usrage)
    except:
        print('!ERROR! enter age in numbers >>')
        continue
    if i_usrage < 100 :
        yrscalc = 100 - i_usrage
        mscalc = yrscalc * 12
        wkscalc = yrscalc
        dyscalc = 365 *  yrscalc
        yrsto100 = 'years to 100: '
        msto100 =  'months to 100: '
        wksto100 = 'weeks to 100: '
        dysto100 = 'days to 100: '
        print(yrsto100.append())
        print(msto100.append())
        print(wksto100.append())
        print(dysto100.append())
        break
    else :
        print('you win life! you have already made it to 100')

print('goodbye', usrname.append('thank you for playing!'))