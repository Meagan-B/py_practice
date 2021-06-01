# Caesar Cipher (caesar.py)
#
# A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. For example, assume the input plain text is the following:
#
# abcd xyz
# If the shift value, n, is 4, then the encrypted text would be the following:
#
# efgh bcd
# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.
#
# Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.
# >>>>>>>>>>>>>>>>>>>>>>>

import string

# ----
def caesar_cipher(t, n) :

    a = string.ascii_lowercase
    new_a = string.ascii_lowercase
    a_shift = (a[0:n])

    for i in a_shift :
        new_a.append(i)

    del new_a[0:n]
    print(a, new_a)
    # ----
    t = [e for e in t]
    # txt_str = ''
    # txt_str = txt_str.join(t)
    # ----
    # alpha_trans = str.maketrans(a, new_a)
    # return t.translate(alpha_trans)
# ----

# org_text = input('enter text to be encoded\n>>> ')
org_alpha = 'abcdefghijklmnopqrstuvwxyz'
# org_text = 'how much wood would a woodchuck chuck if a woodchuck could chuck wood'
cc_num = int(input('enter shift value, for Ceasar Cipher\n>>> '))

# ----

print(caesar_cipher(org_text, cc_num))

# ...........................
