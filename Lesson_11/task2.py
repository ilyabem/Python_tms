#Напишите программу с классом Math. При
#инициализации атрибутов нет. Реализовать методы addition,
#subtraction, multiplication и division. При передаче в методы
#двух числовых параметров нужно производить с
#параметрами соответствующие действия и печатать ответ.

class Math:
    def addition(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtraction(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiplication(self, a, b):
        print(f"{a} * {b} = {a * b}")

    def division(self, a, b):
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Ошибка: деление на ноль!")


# Пример использования
math = Math()
math.addition(5, 3)
math.subtraction(10, 4)
math.multiplication(6, 7)
math.division(8, 2)
math.division(5, 0)