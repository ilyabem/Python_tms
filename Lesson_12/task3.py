 #Класс «Автобус». Класс содержит свойства:
#● скорость
#● максимальное количество посадочных мест
#● максимальная скорость
#● список фамилий пассажиров
#● флаг наличия свободных мест
#● словарь мест в автобусе
#Методы:
#● посадка и высадка одного или нескольких пассажиров
#● увеличение и уменьшение скорости на заданное значение
#● операции in, += и -= (посадка и высадка пассажира по
#фамилии)

class Bus:
     def __init__(self, max_speed, max_seats):
         self.speed = 0
         self.max_speed = max_speed
         self.max_seats = max_seats
         self.passengers = []  # список фамилий пассажиров
         self.seats = {}  # словарь мест в автобусе (место: фамилия)
         self.has_free_seats = True

     def update_free_seats(self):
         """Обновляет флаг наличия свободных мест."""
         self.has_free_seats = len(self.passengers) < self.max_seats

     def board_passenger(self, surname):
         """Посадка пассажира."""
         if self.has_free_seats:
             seat_number = len(self.passengers) + 1
             self.passengers.append(surname)
             self.seats[seat_number] = surname
             self.update_free_seats()
         else:
             print("Автобус полон!")

     def disembark_passenger(self, surname):
         """Высадка пассажира."""
         if surname in self.passengers:
             self.passengers.remove(surname)
             seat_number = list(self.seats.keys())[list(self.seats.values()).index(surname)]
             del self.seats[seat_number]
             self.update_free_seats()
         else:
             print("Пассажир не найден!")

     def change_speed(self, value):
         """Изменяет скорость на заданное значение."""
         self.speed = max(0, min(self.max_speed, self.speed + value))

     def __contains__(self, surname):
         """Оператор in (проверка наличия пассажира)."""
         return surname in self.passengers

     def __iadd__(self, surname):
         """Оператор += (добавление пассажира)."""
         self.board_passenger(surname)
         return self

     def __isub__(self, surname):
         """Оператор -= (удаление пассажира)."""
         self.disembark_passenger(surname)
         return self

     def __str__(self):
         return f"Скорость: {self.speed} км/ч, Пассажиры: {self.passengers}, Свободные места: {self.has_free_seats}"

bus = Bus(100, 3)
bus += "Иванов"
bus += "Петров"
bus += "Сидоров"
bus += "Смирнов"  # Должно вывести "Автобус полон!"

bus -= "Петров"
print(bus)  # Проверим текущее состояние автобуса

bus.change_speed(50)
print(bus)