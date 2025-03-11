'''
a, b, c = map(int, input().split())
mx = 0
mn = 0
if a > b and a > c:
	mx = a
elif b > a and b > c:
	mx = b
elif c> a and c > b:
    mx = c
if a < b and a < c:
	mn = a
elif b < a and b < c:
	mn = b
elif c < a and c < b:
    mn = c
print(mx-mn)

a, b, c = map(int, input().split())
if a+b>=c:
    print(a+b+c)
else:
    print("Impossible")
'''
from curses.textpad import rectangle

'''
a, b, c = map(int, input().split())
mx = 0
if a >= b and a >= c:
	mx = a
elif b >= a and b >= c:
	mx = b
elif c>= a and c >= b:
    mx = c
if 94<=mx<=727:
	print(mx)
	'''
#Задача 1
#Создайте класс Book с атрибутами title и author.
#Затем создайте объект этого класса и выведите его атрибуты.
'''
class Book: # объявляю класс Book
	def __init__(self,title,author): #используя def создаем функцию вызывая
		# метод(конструктор) __init__ для создания нового объекта
		self.title = title # создаем атрибут title(название книги).
		# self - ссылка на текущий объект, который создается.
		self.author = author # создаем атрибут author(автор книги).ё

	def describe(self): # Метод описания книги (должен быть на уровне класса)
			print(f"Книга: {self.title}, Автор: {self.author}")

# Создаем объекты класса Book
book1 = Book("1984", "Джордж Оруэлл")
book2 = Book("Мгла", "Рагнар Йонассон")

# Выводим атрибуты
print(book1.title)
print(book2.author)

# вызовем метод describe
book2.describe()
book1.describe()
'''

#Задача 2
#Создайте класс Dog с атрибутом name.
#Создайте объект класса и измените его атрибут name.
'''
class Dog:
	def __init__(self, name):
		self.name = name
dog1 = Dog("bobik") # Даем объекту имя 
print(dog1.name)
dog1.name = "sharik" # Меняем имя объекта 
print(dog1.name)
'''

#Задача 3
#Создайте класс Circle с атрибутом radius и методом , который возвращает
#длинна круга.
#Создайте объект и вызовите метод.
'''
import math  # Импортируем модуль math для работы с математическими функциями, в том числе с числом π (pi).

class Circle:  # Определяем класс Circle (Круг).
    def __init__(self, radius):  # Метод инициализации (конструктор), который вызывается при создании объекта.
        self.radius = radius  # Присваиваем переданное значение радиуса атрибуту объекта.

    def circumference(self):  # Определяем метод для вычисления длины окружности.
        return 2 * math.pi * self.radius  # Формула длины окружности: C = 2 * π * r.

# Создание объекта класса Circle с радиусом 10.
circle = Circle(10)

# Вызываем метод circumference(), который возвращает длину окружности, и выводим результат в консоль.
print(circle.circumference())  
'''
#Задача 4
#Создайте класс Laptop с атрибутами brand и price.
#Добавьте метод discount, который уменьшает цену на заданный процент.
'''

class Laptop:
	def __init__(self, brand, price):
		self.brand= brand
		self.price = price

	def discount(self, percent):
		self.price -= self.price * (percent/100)
		return self.price


laptop =Laptop("Lenovo", 1000)
print(laptop.discount(10))
'''


#Задача 5
#Создайте класс Rectangle с атрибутами width и height и методом perimeter,
#который возвращает периметр.

'''
class Rectangle:
	def __init__(self, width, height):
		self.width=width
		self.height=height
	def perimetr(self):
		return 2 *(self.width+self.height)
rectangle=Rectangle(11,10)
print(rectangle.perimetr())
'''
#Задача 6
#Создайте класс Student с атрибутами name и grades (список оценок).
#Добавьте метод average_grade, который возвращает среднюю оценку.
'''
class Student:
    def __init__(self, name , grades):
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades)/ len(self.grades) if self.grades else 0

student = Student("Ivan", [90, 85, 78, 92])
print(f"Средний балл {student.name}: {student.average_grade():.2f}")
'''
#Задача 7
#Создайте класс BankAccount с атрибутами balance и методом deposit, который
#увеличивает баланс.
'''
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сумма пополнения должна быть больше нуля")
    def get_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
print("Текущий баланс:", account.get_balance())
'''
#Создайте класс Soda (газировка). Для инициализации
#есть параметр, который определяет вкус газировки. При
#инициализации этот параметр можно задавать, а можно и не
#задавать. Реализовать метод строковой репрезентации,
#который возвращает строку вроде «У вас газировка с
#<клубничным> вкусом», если вкус задан. Если вкус не задан,
#метод должен возвращать строку «У вас обычная газировка».

class Soda:
    def __init__(self, taste = None):
        self.taste = taste
    def show_my_drink(self):
        if self.taste:
            print(f"Газировка со вкусом {self.taste}")
        else:
            print(f"У вас обычная газировка")

drink1= Soda(taste="Клубничный")
drink1.show_my_drink()
