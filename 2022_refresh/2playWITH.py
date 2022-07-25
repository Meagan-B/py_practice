hrs = float(input("Enter Hours:"))
rate = float(input("Enter Pay/Rate:"))

if hrs <= 40 :
    wages = hrs * rate

else :
    reg_wages = 40 * rate
    
    ot_hrs = hrs - 40
    ot_rate = rate * 1.5
    ot_wages = ot_hrs * ot_rate
    
    wages = ot_wages + reg_wages

print(float(wages))