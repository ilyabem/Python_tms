#Программа с классом Car. При инициализации объекта
#ему должны задаваться атрибуты color, type и year.
#Реализовать пять методов. Запуск автомобиля – выводит
#строку «Автомобиль заведён». Отключение автомобиля –
#выводит строку «Автомобиль заглушен». Методы для
#присвоения автомобилю года выпуска, типа и цвета.

class Car:
    def __init__(self, color, type, year):
        self.color=color
        self.type=type
        self.year=year
        self.enigne_on = False

    def start_enigne(self):
        if self.enigne_on:
            print('Авто уже запущено')
        else:
            print('Авто заведено')

    def stop_enigne(self):
        if not self.enigne_on:
            print('Авто уже заглушено')
        else:
            self.enigne_on = False
            print('Двигатель заглушен')


    def set_color(self, color):
        self.color=color


    def set_type(self, type):
        self.type=type

    def set_year(self,year):
        self.year = year

car = Car("Черный", "Пикап", '2020')
car.start_enigne()
car.start_enigne()
car.stop_enigne()
car.stop_enigne()