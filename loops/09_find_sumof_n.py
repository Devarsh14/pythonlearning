number = int(input("Enter a number: "))
sum = 0
count = 1
while count <= number:
    print(f"{sum} + {count}")
    sum +=count
    print(f"SUM: {sum}")
    count += 1
print(f"The sum of {number} is {sum}")