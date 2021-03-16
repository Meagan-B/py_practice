#Write a program to prompt the user for hours and rate per hour using input
#with 1.5% overtime
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# defining a function to calculate pay
def pay_calc(hours, rate) :
    # if the user inputs hours over 40 we follow this if path
    if hours >40 :
        # var reg is equal to rate • hours (both input by user)
        reg = rate * hours
        #  this calculates overtime pay (represented as var otp),
        otp = (hours - 40) * (rate * 1.5)
        # x represents our total, regular pay and overtime pay
        x = reg + otp
        # returns the string 'Pay' and the value of variable x
        print('Pay', x)
    # for cases where the hours are under 40 or equal to 40, everything but >40
    else :
        # variable x will hold the value of regular pay
        x = reg
        print('Pay', x)
# ?????????????????????????
    return x
# ?????????????????????????

# a try loop to handle the user inputs
try :
    hrs = float(input('hours: '))
    r = float(input('hourly rate: '))
# ?????????????????????????
except :
    print('numbers only')
# ?????????????????????????


# calls our defined function pay_calc (above^)
pay = pay_calc(hrs,r)
