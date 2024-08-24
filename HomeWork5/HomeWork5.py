import string
user_input = input("Enter range a letters. Example:b-C: ")
start_letter = user_input[0]
end_letter = user_input[-1]

start_index = string.ascii_letters.find(start_letter)
end_index = string.ascii_letters.find(end_letter)

final_string = string.ascii_letters[start_index:end_index+1]

print(final_string)



