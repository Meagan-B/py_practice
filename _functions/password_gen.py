#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#

#----••••••••----••••••••----••••••••----#
print('~~~~ PASSWORD GENERATOR ~~~~\n\nSTRONG passwords will consist of 15, randomly selected, characters\n\nWEAK passwords will consist of 3, randomly selected, english words\n\n••••••••••••••••••••\n\n')
#----••••••••----••••••••----••••••••----# 
def pass_generator(n) :
    import random
    import string
    #from english_words import english_words_alpha_set
#----••••••••----#
    n = int(n)
#----••••••••----#
    pass_gen = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for char in range(n+1)])
    return pass_gen
#----••••••••----••••••••----••••••••----# 
pass_rating = input('enter your desired password length below\n>>> ')
print(pass_generator(pass_rating))
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
