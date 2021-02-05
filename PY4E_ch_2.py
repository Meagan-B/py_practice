#Write a program to prompt the user for hours and rate per hour using input

try :
    hrs = int(input('Hours: '))
    rate = float(input('Rate/Hour: '))
except :
    print('numbers only')

print('Pay: ', hrs * rate)
