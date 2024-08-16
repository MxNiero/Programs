import keyword
import string

punctuation_marks = string.punctuation
my_marks = []

for marks in punctuation_marks:
    my_marks.append(marks)
my_marks.remove("_")
my_marks.append(" ")

user_variable = input("Enter name variable: ")

if user_variable.count("_") > 1:
    print(False)
    exit()

if user_variable[0].isdigit():
    print(False)
    exit()

for upper_char in user_variable:
    if upper_char.istitle():
        print(False)
        exit()

for char in user_variable:
    if char in my_marks:
        print(False)
        exit()


if user_variable in keyword.kwlist:
    print(False)
    exit()

if user_variable.isalpha():
    print(True)
    exit()


elif user_variable[0].istitle():
    print(False)
    exit()

print(True)


