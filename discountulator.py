# calculate the discount, excluding taxes
# with user input for cart total, discount rate and discount minimum requirements
try :
    user_cart = float(input('enter cart total: '))
    user_discount_rate = float(input('enter discount "_% off": '))
    user_discount_min = float(input('enter discount minimum, use 0 for no discount minimum: ' ))
except :
    print('enter numbers only')

if user_discount_min == 0 :
    print(user_discount_rate * user_cart)
    print((user_discount_rate * user_cart) / user_cart)
    print( 20 * 200 / 100)

#else :
    #ot = (hrs - 40) * (rate * 1.5)
    #print('Overtime Pay: ', (40 * rate) + ot)
