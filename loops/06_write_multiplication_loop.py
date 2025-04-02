n = input("Enter a number: ")
for i in range (1, 11):
    print(f"{n} x {i} = {int(n) * i}")

t = 1
while t<11:
    print(f"{n} x {t} = {int(n) * t}")
    t += 1