#Exercise 1: Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.


fruit = 'pineapple'
#print(len(fruit))

index = -1
for letter in fruit :
    if index < len(fruit) :
        letter = fruit[index]
        print(letter)
        index = index - 1
    elif index > len(fruit) :
        break
#while index :
print('end')
