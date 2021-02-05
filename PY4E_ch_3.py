#Write a program to prompt the user for hours and rate per hour using input
#with 1.5% overtime

try :
    hrs = float(input('Hours: '))
    rate = float(input('Hourly Rate: '))
except :
    print('numbers only')

if hrs <= 40 :
    print('Regular Pay: ', hrs * rate)

else :
    ot = (hrs - 40) * (rate * 1.5)
    print('Overtime Pay: ', (40 * rate) + ot)
