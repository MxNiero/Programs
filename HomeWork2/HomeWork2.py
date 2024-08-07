user_input = int(input("Enter a number: "))
user_action = input("Select an action: + - / * : ")
user_second_input = int(input("Enter a second number :"))

if user_action == "+":
    print(user_input + user_second_input)

if user_action == "-":
    print(user_input - user_second_input)

if user_action == "/":
    if user_second_input == 0:
        print("Division by zero")
    else:
        print(float(user_input) / user_second_input)

if user_action == "*":
    print(user_input * user_second_input)