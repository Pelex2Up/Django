class SimpleCalc:

    def __init__(self):
        self.input_data()

    def input_data(self):
        self.num1 = int(input('Введите 1-е число: '))
        self.num2 = int(input('Введите 2-е число: '))

    def summa(self):
        return self.num1 + self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def segmentation(self):
        if self.num2 == 0:
            return 'Error'
        else:
            return self.num1 / self.num2

    def subtraction(self):
        return self.num1 - self.num2


while True:
    calc = SimpleCalc()
    operator = input("Введите операцию: ")
    if operator == '+': print(calc.summa())
    elif operator == '-': print(calc.subtraction())
    elif operator == '*': print(calc.multiplication())
    elif operator == '/': print(calc.segmentation())
