# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# >>>>>>>>>>>>>>>>>>>>>

import random
import string

# ----

pass_rating = input('how strong of a password would you like?\nenter WEAK or STRONG below\n>>> ')

# ----

printable = string.printable
# print(printable)




# ----

# weak_pass =
strong_pass = [random.choice(printable) for char in range(15)]
strong_pass = ''.join(strong_pass)

print(len(strong_pass), strong_pass)


# ----

# ----
# if pass_rating == 'WEAK' or pass_rating == 'weak' :

# elif pass_rating == 'STONG' or pass_rating 'strong' :

# ----


# ...........................
