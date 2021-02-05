print("START")

for user_input in range(1, 101):
    if user_input % 3 == 0 and user_input % 5 == 0:
        str = "{}) fizzbuzz"
        print (str.format(user_input))

    elif user_input % 3 == 0:
        str = "{}) fizz"
        print (str.format(user_input))

    if user_input % 5 == 0:
        str = "{}) buzz"
        print (str.format(user_input))

print("FIN")        



# user_input = 15

# if user_input % 3 == 0: 
#     print(“FIZZ”)

# if user_input % 5 == 0:
#     print (“BUZZ”)

# if user_input % 3 == 0 and user_input % 5 == 0:
#     print (“FIZZBUZZ”)