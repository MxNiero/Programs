class NumberStudentsException(Exception):
    print("Number students more than 10")


class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_mame = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, First name: {self.first_mame}, Last name: {self.last_name}, "


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


class Group:

    def __init__(self, number, count=0):
        self.number = number
        self.group = set()
        self.count = count

    def add_student(self, student):
        if self.count > 9:
            raise NumberStudentsException
        else:
            self.group.add(student)
            self.count += 1

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = "\n".join([f"{student}" for student in self.group])
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN140')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN141')
st3 = Student('Male', 92, 'Hank', 'Wood', 'AN142')
st4 = Student('Female', 83, 'Ann', 'Ohaio', 'AN143')
st5 = Student('Male', 37, 'Big', 'Diddy', 'AN144')
st6 = Student('Male', 46, 'Kile', 'Crein', 'AN145')
st7 = Student('Male', 58, 'Woody', 'Woodpeker', 'AN146')
st8 = Student('Male', 27, 'Aleksandr', 'Baker', 'AN147')
st9 = Student('Male', 17, 'Vitalii', 'Rodriges', 'AN148')
st10 = Student('Male', 44, 'Jason', 'Stethem', 'AN149')
st11 = Student('Male', 18, 'Luffy', 'Monkey', 'AN150')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except NumberStudentsException as e:
    print(e, "\n")


print(gr, "\n")
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
