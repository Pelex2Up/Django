class Students:
    stud_data = dict()

    def __init__(self, sname_and_initials, num_grp, efficiency):
        self.sname_and_initials = sname_and_initials
        self.num_grp = num_grp
        self.efficiency = efficiency
        self.stud_data.update({self.sname_and_initials: [self.num_grp, self.efficiency]})


class School:

    def __init__(self, students):
        self.students = dict(students)

    def add_stud(self, secname_and_init, numb_of_grp, grades):
        self.students.update({secname_and_init: [numb_of_grp, grades]})

    def get_stud_by_grade(self, grade):
        for k, i in self.students.items():
            if sum(i[1]) / len(i[1]) == grade:
                print(f'Студент {k} имеет средний балл {grade}.')

    def get_grp(self, grp):
        print(f'Студенты из группы {grp}:')
        for k, i in self.students.items():
            if i[0] == grp:
                print(f'{k}')

    def if_auto(self):
        print(f'Студенты претендующие на автомат:')
        for k, i in self.students.items():
            if sum(i[1]) / len(i[1]) >= 7:
                print(f'{k}, средний балл: {sum(i[1]) / len(i[1])}.')


stud_1 = Students('Прохоренко Б.А.', 10606113, [6, 8, 5, 4, 4])
stud_2 = Students('Семенюк К.Ю.', 10603114, [8, 7, 9, 10, 7])

stud_base = School(Students.stud_data)
stud_base.add_stud('Name', 102013012, [4, 4, 4, 4, 4])

stud_base.if_auto()
print()
stud_base.get_grp(10606113)
print()
stud_base.get_stud_by_grade(4)

