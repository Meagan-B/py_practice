hrs = float(input("Enter Hours:"))
rate = float(input("Enter Pay/Rate:"))

if hrs <= 40 :
    wages = hrs * rate


else :
    rate = rate * 1.5
    wages = hrs * rate
