class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_mame = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, First name: {self.first_mame}, Last name: {self.last_name}, "
