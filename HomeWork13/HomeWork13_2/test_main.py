from HomeWork13.HomeWork13_2.moduls import class_student, group

st1 = class_student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = class_student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = group.Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
