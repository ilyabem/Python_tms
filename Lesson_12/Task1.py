#Класс «Товар» содержит следующие закрытые поля:
#● название товара
#● название магазина, в котором подаётся товар
#● стоимость товара в рублях
#Класс «Склад» содержит закрытый массив товаров.
#Обеспечить следующие возможности:
#● вывод информации о товаре со склада по индексу
#● вывод информации о товаре со склада по имени товара
#● сортировка товаров по названию, по магазину и по цене
#● перегруженная операция сложения товаров по цене

class Product:
    def __init__(self, name, store, price):
        #Конструктор: принимает название, магазин и цену товара
        self._name = name  # Закрытое поле: название товара
        self._store = store  # Закрытое поле: название магазина
        self._price = price  # Закрытое поле: цена товара

    def __str__(self):
        #Вывод информации о товаре
        return f"Товар: {self._name}, Магазин: {self._store}, Цена: {self._price} руб."

    def get_name(self):
        #Возвращает название товара
        return self._name

    def get_store(self):
        #Возвращает название магазина
        return self._store

    def get_price(self):
        #Возвращает цену товара
        return self._price

    def __add__(self, other):
        #Перегруженный оператор сложения: складывает цены товаров
        if isinstance(other, Product):  # Проверяем, является ли объект товаром
            return self._price + other._price  # Складываем цены товаров
        raise TypeError("Можно складывать только товары!")  # Ошибка, если сложение с чем-то другим




class Warehouse:
    def __init__(self):
        #Конструктор: создаем пустой склад (список товаров)
        self._products = []  # Закрытый список товаров

    def add_product(self, product):
        #Добавляет товар на склад
        if isinstance(product, Product):  # Проверяем, что добавляем именно товар
            self._products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product!")

    def get_product_by_index(self, index):
        #Выводит информацию о товаре по индексу
        if 0 <= index < len(self._products):  # Проверяем, что индекс в допустимом диапазоне
            return str(self._products[index])  # Возвращаем информацию о товаре
        return "Товар с таким индексом отсутствует"

    def get_product_by_name(self, name):
        #Выводит информацию о товаре по названию
        for product in self._products:  # Перебираем все товары на складе
            if product.get_name() == name:
                return str(product)  # Возвращаем товар, если найден
        return "Товар с таким названием отсутствует"

    def sort_by_name(self):
        #Сортирует товары по названию
        self._products.sort(key=lambda product: product.get_name())  # Сортируем по имени

    def sort_by_store(self):
        #Сортирует товары по магазину
        self._products.sort(key=lambda product: product.get_store())  # Сортируем по магазину

    def sort_by_price(self):
        #Сортирует товары по цене
        self._products.sort(key=lambda product: product.get_price())  # Сортируем по цене

    def __str__(self):
        #Выводит все товары на складе
        return "\n".join(str(product) for product in self._products)  # Перебираем все товары и соединяем их в строку


# === Тестирование ===

# Создаем товары
p1 = Product("Ноутбук", "Техносила", 50000)
p2 = Product("Смартфон", "Онлайнер", 30000)
p3 = Product("Планшет", "5 элемент", 20000)

# Создаем склад
warehouse = Warehouse()

# Добавляем товары на склад
warehouse.add_product(p1)
warehouse.add_product(p2)
warehouse.add_product(p3)

# Выводим товары со склада
print("=== Товары на складе ===")
print(warehouse)

# Получаем товар по индексу
print("\nТовар по индексу 1:")
print(warehouse.get_product_by_index(1))

# Получаем товар по названию
print("\nТовар по названию 'Ноутбук':")
print(warehouse.get_product_by_name("Ноутбук"))

# Сортируем товары по цене и выводим
warehouse.sort_by_price()
print("\n=== Товары после сортировки по цене ===")
print(warehouse)

# Сложение цен двух товаров
print("\nСложение цен ноутбука и смартфона:")
print(p1 + p2)  # Выведет 80000


