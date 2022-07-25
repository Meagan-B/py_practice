hrs = float(input("Enter Hours:"))
rate = float(input("Enter Pay/Rate:"))

if hrs <= 40 :
    wages = hrs * rate


else :
    print(rate)
    rate = rate * 1.5
    print(rate)
    wages = hrs * rate

print(float(wages))