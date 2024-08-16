import string
hastag = "#"

user_input = input("Enter hastag: ")

print()
user_input = user_input.title()

for symbol in string.punctuation:
    user_input = user_input.replace(symbol, "")

for space in user_input:
    if space == " ":
        user_input = user_input.replace(space, "")

if len(user_input) > 140:
    user_input = user_input[:140]

print(f"{hastag}{user_input}")
