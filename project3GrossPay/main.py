hours = float(input(f"Enter hours worked: "))
rate = float(input(f"Enter Rate: "))
# calculate gross pay
grossPay = round(hours * rate,2)
print(f"Gross pay is: {grossPay}")