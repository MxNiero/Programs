end = bool(True)
while end:
    user_input = int(input("Enter a number: "))
    user_action = input("Select an action: + - * / : ")
    user_second_input = int(input("Enter a second number :"))

    if user_action == "+":
        print(user_input + user_second_input)

    elif user_action == "-":
        print(user_input - user_second_input)

    elif user_action == "*":
        print(user_input * user_second_input)

    elif user_action == "/" and user_second_input != 0:
        print(float(user_input) / user_second_input)
    else:
        print("Division by zero")

    end = input("Do you want finish? yes/no: ")

    if end == "yes":
        end = bool(False)
    else:
        end = bool(True)



