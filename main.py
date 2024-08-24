import math

my_number = int(input("Enter number: "))

for number in range(1, my_number+1):
    result = math.pow(number, 2)
    if result < my_number:
        print(round(result), end=" ")
    else:
        break


