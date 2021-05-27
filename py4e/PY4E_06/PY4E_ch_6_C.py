#Exercise 3: Encapsulate this code in a function named count, and generalize
#it so that it accepts the string and the letter as arguments.

word = 'banana'

def counter() :
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count, letter + "'s")

counter()
