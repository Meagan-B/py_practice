#Write a program to prompt the user for hours and rate per hour using input
#with 1.5% overtime
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# defining a function to calculate pay, if the user inputs hours over 40 we follow if path. var reg is equal to rate • hours (both input by user), otp calculates overtime pay, x represents our total. for cases where the hours are under 40 or equal to 40, everything but >40, variable x will hold the value of regular pay,
def pay_calc(hours, rate) :
    if hours >40 :
        reg = rate * hours
        otp = (hours - 40) * (rate * 1.5)
        x = reg + otp
        print('Pay', x)
    else :
        x = reg
        print('Pay', x)
    return x

#----
# a try loop to handle the user inputs
try :
    hrs = float(input('hours: '))
    r = float(input('hourly rate: '))
except :
    print('numbers only')

#----
# calls our defined function pay_calc (above^)
pay = pay_calc(hrs,r)

#....................
