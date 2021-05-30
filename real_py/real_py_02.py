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

def caesar_cipher(t, n) :




# ----

org_text = input('enter text to be encoded\n>>> ')
cc_num = int(input('enter shift value, for Ceasar Cipher\n>>> '))

# ----

caesar_cipher(org_text, cc_num)

# ...........................
