import string

user_input = input("Enter hastag: ")


for symbol in string.punctuation:
    user_input = user_input.replace(symbol, "")

user_input = user_input.title()

user_input = user_input.replace(" ", "")

if len(user_input) > 140:
    user_input = user_input[:140]

print(f"#{user_input}")
