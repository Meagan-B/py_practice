# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# >>>>>>>>>>>>>>>>>>>>>

import random
import string
from english_words import english_words_alpha_set

# ----

print('~~~~ PASSWORD GENERATOR ~~~~\n\nSTRONG passwords will consist of 15, randomly selected, characters\n\nWEAK passwords will consist of 3, randomly selected, english words\n\n••••••••••••••••••••\n\n')

# ----

pass_rating = input('how strong of a password would you like?\n\nenter W/w for a WEAK password\nenter S/s for a STRONG password\n\n>>> ')

# ----
eng_set_lst = list(english_words_alpha_set)
words = []
count = 0

while count < 3 :
    words.append(random.choice(eng_set_lst))
    count += 1

weak_pass = ''.join(words)
# print(words)

# ----

strong_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for char in range(25)])

# ----

if pass_rating == 'W' or pass_rating == 'w':
    # print(pass_rating)
    print('your {0} password below\n{1}'.format(pass_rating, weak_pass))
elif pass_rating == 'S' or pass_rating == 's' :
    # print(pass_rating)
    print('your {0} password below\n{1}'.format(pass_rating, strong_pass))
# else :
    # print('butt')






# ...........................
