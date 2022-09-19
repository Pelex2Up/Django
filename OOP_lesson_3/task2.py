# Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента. Класс студен описан следующим образом:
# Необходимо понять у кого больше всего денег и вернуть его имя. Если у студентов денег поровну вернуть: “all”.
class Student:
    data = dict()

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.data.update({name: money})


student_1 = Student('David', 2500)
student_2 = Student('Karl', 500)
student_3 = Student('Kimberly', 1600)
student_4 = Student('Helen', 2501)

val = set(Student.data.values())
if len(val) > 1:
    for k, v in Student.data.items():
        if v == max(Student.data.values()):
            print(f'Студент с наибольшим количеством денег: {k}. На балансе: {v}$.')
else:
    print(f'All')