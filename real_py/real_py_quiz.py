import re

def letter_changes(my_string):
    in_letters = "abcdefghijklmnopqrstuvxyz"
    out_letters = "bcdefghijklmnopqrstuvxyza"

    letter_dict1 = {x:y for x,y in zip(in_letters, out_letters)}
    letter_dict2 = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U'}

    for l_dict in [letter_dict1, letter_dict2]:
        pattern = re.compile("|".join(l_dict.keys()))
        my_string = pattern.sub(lambda m: l_dict[re.escape(m.group(0))], my_string)

    return my_string

print(letter_changes('fork'))