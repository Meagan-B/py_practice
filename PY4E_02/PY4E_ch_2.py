#Write a program to prompt the user for hours and rate per hour using input
======
#2.3 Write a program to prompt the user
#for hours and rate per hour using input
======
# begining of try loop, where C will attempt the prompts below try and above accept
try :
    # hrs variable will contain an integer given to C by user via the input() funtion, here a total number of hours
    hrs = int(input('hours: '))
    # rate variable will contain a float given to C by user via the input() funtion, here an hourly rate
    rate = float(input('hourly rate: '))
# if the try fails except will take over, maybe user enters a character instead of a number, this is a broad except and I need to spend
# ?????????????????????????
# additional time learning more about exceptions
except :
# ?????????????????????????    
    # returns the argument inside () here that is a string, 'numbers only', this functions as a custom error message
    print('numbers only')

print('pay: ', hrs * rate)
