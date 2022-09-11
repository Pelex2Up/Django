class TheExample:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def create_per(self):
        self.c = int(input('Введите значение для переменной: '))
        print(self.c)

    def sum_per(self):
        return self.a + self.b

    def some_func(self):
        return self.t ** self.r


example = TheExample(4, 2)
print(example.a)
print(example.some_func())
print(example.sum_per())
example.create_per()