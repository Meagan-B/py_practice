# calculate the discount, excluding taxes
# with user input for cart total, discount rate and discount minimum requirements
try :
    inp_cart = float(input('enter cart total: '))
    inp_discount_rate = float(input('enter discount "_% off": '))
    inp_discount_min = float(input('enter discount minimum, use 0 for no discount minimum: ' ))
except :
    print('enter numbers only')

if inp_discount_min == 0 :
    user_discount_total = ((inp_discount_rate / 100) * inp_cart)
    print('you saved: ', user_discount_total)
    print('new total: ', inp_cart - user_discount_total)
elif inp_discount_min >= 0 and inp_discount_min <= inp_cart:
    user_discount_total = ((inp_discount_rate / 100) * inp_cart)
    print('you saved: ', user_discount_total)
    print('new total: ', inp_cart - user_discount_total)
else :
    print('you have not met the minimum cart total to qualify for a discount')

#else :
    #ot = (hrs - 40) * (rate * 1.5)
    #print('Overtime Pay: ', (40 * rate) + ot)
