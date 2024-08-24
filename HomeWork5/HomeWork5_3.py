user_input = int(input("Enter a number: "))

while user_input > 9:
    result = 1
    while user_input > 0:
        result *= user_input % 10
        user_input //= 10
    user_input = result

print(user_input)


