# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# >>>>>>>>>>>>>>>>>>>>>

import random
import string
from english_words import english_words_set

# ----

print('~~~~ PASSWORD GENERATOR ~~~~\nSTRONG passwords will consist of 15, randomly selected, characters\nWEAK passwords will consist of 3, randomly selected, english words\n••••••••\n')

# ----
# pass_rating = input('how strong of a password would you like?\nenter WEAK or STRONG below\n>>> ')


# ----

# if pass_rating == 'WEAK' or pass_rating == 'weak' :

# words = english_words_alpha_set
print(english_words_alpha_set)

# weak_pass = ''.join([random.choice(words) for wrd in range(3)])

# print('your {0} password below\n{1}'.format(pass_rating, weak_pass))


# ----
# elif pass_rating == 'STONG' or pass_rating 'strong' :


# strong_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for char in range(15)])


# print('your {0} password below\n{1}'.format(pass_rating, strong_pass))


#


# ...........................
