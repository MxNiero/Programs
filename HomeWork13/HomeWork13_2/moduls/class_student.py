from HomeWork13.HomeWork13_2.moduls.class_human import Human


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.gender = gender
        self.age = age
        self.first_mame = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return (f"Gender: {self.gender}, Age: {self.age}, First name: {self.first_mame}, Last name: {self.last_name}, "
                f"Record book: {self.record_book}")

    def __hash__(self):
        return hash(str(self))

