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
import re

# ----

def caesar_cipher(t, n) :

    in_alpha = string.ascii_lowercase
    out_alpha = list(in_alpha)
    alpha_shift = (out_alpha[0:n])

    for i in alpha_shift :
        out_alpha.append(i)

    del out_alpha[0:n]
    
    out_alpha_str = ''
    out_alpha = out_alpha_str.join(out_alpha)
    
# ----

    #t = [e for e in t]
    #print(t)
    
    letter_dict1 = {x:y for x,y in zip(in_alpha, out_alpha)}
    #print(letter_dict1)
    
    #txt_str = ''
    #txt_str = txt_str.join(t)
    #print(txt_str)
    
    # NEED MORE INFO< CODE FROM O_STACK
    for l_dict in [letter_dict1]:
        pattern = re.compile("|".join(l_dict.keys()))
        #print(pattern)
        my_string = pattern.sub(lambda m: l_dict[re.escape(m.group(0))], t)
        #print(my_string)
    
    return my_string
# ----

org_text = input('enter text to be encoded\n>>> ')
#org_text = 'how much wood would a woodchuck chuck if a woodchuck could chuck wood'
cc_num = int(input('enter shift value, for Ceasar Cipher\n>>> '))

# ----

#print(caesar_cipher(org_text, cc_num))
print('ORIGINAL TEXT: {0}'.format(org_text))
print(caesar_cipher(org_text, cc_num))

# ...........................
