import string


def is_palindrome(text: str) -> True or False:
    text = text.lower()
    for marks in text:
        if marks in string.punctuation:
            text = text.replace(marks, "")
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
