#2.3 Write a program to prompt the user
#for hours and rate per hour using input
try :
    hrs = float(input('Hours: '))
    rate = float(input('Rate/Hour: '))
except :
    print('numbers only')

if hrs <= 40:
    print('regular pay: ', hrs * rate)
else :
    ot = (hrs - 40) * (rate * 1.5)
    print('overtime pay: ', (40 * rate) + ot)
