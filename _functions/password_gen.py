#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
print('~~~~~ PASSWORD GENERATOR ~~~~~\n••••••••••••••••••••••••••••••')
#----••••••••----••••••••----••••••••----# 
def pass_generator(n) :
    import random
    import string
    #from english_words import english_words_alpha_set
#----••••••••----#
    n = int(n)
    if n < 8 :
        n = 8
#----••••••••----#
    pass_gen = ''.join([random.choice(string.ascii_letters + string.digits + '!' + '-' ) for char in range(n)])
    return pass_gen
#----••••••••----••••••••----••••••••----# 
pass_rating = input('enter desired password length\n>>> ')
print(pass_generator(pass_rating))
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
