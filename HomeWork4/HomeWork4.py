import keyword
import string

user_variable = input("Enter name variable: ")
result = "\nTrue"

for marks in user_variable:
    if marks in string.punctuation and marks != "_" or marks == " ":
        result = result.replace("True", "False")

if user_variable.count("_") == len(user_variable) > 1:
    print(False)

elif user_variable[0].isdigit():
    print(False)

elif user_variable in keyword.kwlist:
    print(False)

elif not user_variable.islower() and user_variable != "_":
    print(False)

else:
    print(result)
