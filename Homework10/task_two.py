import math


class Student():
    def __init__(self, lastname, name, group_number, academic_performance):
        self.lastname = lastname
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance

    def __repr__(self):
        return f"{self.lastname} {self.name}"

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        if not isinstance(lastname, str):
            raise TypeError('lastname a must be string')
        self._lastname = lastname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name a must be string')
        self._name = name


class School():
    students = []

    def add_student(self, student):
        self.students.append(student)

    def get_best_students(self):
        best_students_list = []
        for student in self.students:
            have_best_mark = False
            for mark in student.academic_performance:
                if mark == 5 or mark == 6:
                    have_best_mark = True
                    break
            if have_best_mark:
                best_students_list.append({
                    'lastname': student.lastname,
                    'group': student.group_number
                    })
        return best_students_list

    def get_students(self, group_number):
        students_in_group = []
        for student in self.students:
            if student.group_number == group_number:
                students_in_group.append(student)
        return students_in_group

    def get_students_without_exams(self):
        best_students_without_exams_list = []
        for student in self.students:
            marks = student.academic_performance
            avg_mark = math.fsum(marks) / len(marks)
            if avg_mark >= 7:
                best_students_without_exams_list.append({
                    'lastname': student.lastname,
                    'name': student.name
                    })
        return best_students_without_exams_list


first_student = Student('Ivanov', 'Ivan', 10, [1, 2, 3, 4, 5])
second_student = Student('Petrov', 'Petr', 20, [5, 7, 10, 8, 9])
third_student = Student('Sidorov', 'Sidor', 10, [2, 3, 4, 5, 6])
print(first_student.lastname)

school1 = School()
school1.add_student(first_student)
school1.add_student(second_student)
school1.add_student(third_student)

print('students', school1.students)
print('best students', school1.get_best_students())
print('students from schcool', school1.get_students(10))
print('students_without_exams', school1.get_students_without_exams())
