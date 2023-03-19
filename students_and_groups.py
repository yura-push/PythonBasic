class Group:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.group_list = []

    def get_name(self):
        return f"{self.__group_name}"

    def add_students(self, students):
        [self.group_list.append(student) for student in students]

    def get_students(self):
        return self.group_list

    def get_student(self, student_num):
        return self.group_list[student_num]

    def del_students(self, param):
        for student in self.group_list:
            if student == param:
                self.group_list.pop(student)

    def __str__(self):
        return f"{self.__group_name}"


class Student:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__grades = []

    def get_name(self):
        return f"{self.__name}"

    def get_surname(self):
        return f"{self.__surname}"

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_grades(self):
        return self.__grades

    def set_grades(self, grades_lst):
        self.__grades = grades_lst

    def __str__(self):
        return f"{self.__name} {self.__surname}"


if __name__ == "__main__":
    student_1 = Student("Bob", "Brown")
    student_2 = Student("Carl", "Jonson")
    student_3 = Student("Peter", "Parker")

    assert getattr(student_1, "name", None) is None
    assert getattr(student_2, "name", None) is None
    assert getattr(student_3, "name", None) is None

    assert getattr(student_1, "surname", None) is None
    assert getattr(student_2, "surname", None) is None
    assert getattr(student_3, "surname", None) is None

    assert getattr(student_1, "grades", None) is None
    assert getattr(student_2, "grades", None) is None
    assert getattr(student_3, "grades", None) is None

    assert student_1.get_name() == "Bob"
    assert student_1.get_surname() == "Brown"

    assert student_2.get_name() == "Carl"
    assert student_2.get_surname() == "Jonson"

    assert student_3.get_name() == "Peter"
    assert student_3.get_surname() == "Parker"

    student_1.add_grade(1)
    assert len(student_1.get_grades()) == 1
    student_1.add_grade(2)
    assert len(student_1.get_grades()) == 2

    lst_grades = [8, 10, 9, 7, 6, 5]
    student_1.set_grades(lst_grades)
    assert len(student_1.get_grades()) == len(lst_grades)
    assert set(student_1.get_grades()) == set(lst_grades)

    lst_grades = [10, 8, 6, 5, 7, 6]
    student_2.set_grades(lst_grades)
    assert len(student_2.get_grades()) == len(lst_grades)
    assert set(student_2.get_grades()) == set(lst_grades)

    lst_grades = [12, 9, 5, 8, 10, 8]
    student_3.set_grades(lst_grades)
    assert len(student_3.get_grades()) == len(lst_grades)
    assert set(student_3.get_grades()) == set(lst_grades)

    assert student_1.get_name() in str(student_1)
    assert student_2.get_name() in str(student_2)
    assert student_3.get_name() in str(student_3)

    assert student_1.get_surname() in str(student_1)
    assert student_2.get_surname() in str(student_2)
    assert student_3.get_surname() in str(student_3)

    print(student_1)
    print(student_2)
    print(student_3)

    group = Group("#1")
    assert group.get_name() == "#1"
    assert getattr(group, "name", None) is None

    group.add_students([student_1, student_2, student_3])
    assert len(group.get_students()) == 3
    assert group.get_student(0).get_name() == student_1.get_name()
    assert getattr(group, "students", None) is None

    print(group)
    print()

    group.del_students([student_1])
    print(group)
    print()

    group_2 = Group("#2")
    assert group_2.get_name() == "#2"
    assert getattr(group_2, "name", None) is None

    group_2.add_students([student_3])

    assert len(group_2.get_students()) == 1
    assert group_2.get_student(0).get_name() == student_3.get_name()
    assert getattr(group_2, "students", None) is None
    print(group_2)