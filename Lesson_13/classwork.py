
#**Создайте класс Dog** с атрибутами name и breed, добавьте метод bark(), который печатает "Гав-гав!"
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("ГАВ-ГАВ")

dog1 = Dog("Шарик", "Лабрадор")
dog1.bark()

a, b, c = map(int, input().split())