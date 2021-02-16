#Write a program to prompt the user for hours and rate per hour using input
#with 1.5% overtime


#try :
    #hrs = float(input('hours: '))
    #rate = float(input('hourly rate: '))
#except :
    #print('numbers only')

#def reg_pay_calc () :
    #total_reg_pay = hrs * rate
    #print(total_reg_pay)

#if hrs <= 40 :
    #print('regular pay:')
    #reg_pay_calc()
#else :
    #ot = (hrs - 40) * (rate * 1.5)
    #print('overtime pay:')
    #reg_pay_calc(+ ot)
    #print('overtime pay: ', (40 * rate) + ot)
def pay_calc(hours, rate) :
    if hours >40 :
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        x = reg + otp
        print('Pay', x)
    else :
        x = reg
        print('Pay', x)
    return x

try :
    hrs = float(input('hours: '))
    r = float(input('hourly rate: '))
except :
    print('numbers only')

    
pay = pay_calc(hrs,r)
