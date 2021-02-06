#Write a program to prompt the user for hours and rate per hour using input
======
#2.3 Write a program to prompt the user
#for hours and rate per hour using input
======

try :
    hrs = int(input('hours: '))
    rate = float(input('hourly rate: '))
except :
    print('numbers only')

print('pay: ', hrs * rate)
