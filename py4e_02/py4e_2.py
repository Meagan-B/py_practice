#Write a program to prompt the user for hours and rate per hour using input
======
#2.3 Write a program to prompt the user
#for hours and rate per hour using input
======
# begining of try loop, where C will attempt the prompts below try and above accept
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# hrs variable will contain an integer given by user via the input() funtion, here it is total hours worked. rate variable will contain a float given by user via the input() funtion, here an hourly rate. if the try fails, except will take over, maybe user enters a character instead of a number, this is a broad except.
try :
    hrs = int(input('hours: '))
    rate = float(input('hourly rate: '))
except :
    print('numbers only')

#----

print('pay: ', hrs * rate)

#.........................
