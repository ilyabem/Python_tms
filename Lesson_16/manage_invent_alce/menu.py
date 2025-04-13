from db import session
from models import Category, Supplier, Product, SupplyOrder
from datetime import datetime

def add_product(name, quantity, price, category_name, supplier_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)

    supplier = session.query(Supplier).filter_by(name=supplier_name).first()
    if not supplier:
        supplier = Supplier(name=supplier_name, contact="")
        session.add(supplier)

    product = Product(name=name, quantity=quantity, price=price,
                      category=category, supplier=supplier)
    session.add(product)
    session.commit()
    print(f"Товар {name} добавлен.")

def edit_product(name):
    product = session.query(Product).filter_by(name=name).first()
    if not product:
        print("Товар не найден.")
        return
    product.price = float(input("Новая цена: "))
    product.quantity = int(input("Новое количество: "))
    session.commit()
    print("Товар обновлен.")

def delete_product(name):
    product = session.query(Product).filter_by(name=name).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"Товар {name} удален.")
    else:
        print("Товар не найден.")

def find_products_by_category(category_name):
    category = session.query(Category).filter(Category.name.ilike(f"%{category_name}%")).first()
    if category:
        for product in category.products:
            print(f"{product.name} — {product.quantity} шт. — {product.price} BYN")
    else:
        print("Категория не найдена.")

def search_by_name(model, name_part):
    results = session.query(model).filter(model.name.ilike(f"%{name_part}%")).all()
    for r in results:
        print(f"{r.name}")

def warehouse_report():
    products = session.query(Product).all()
    for p in products:
        print(f"{p.name} — {p.quantity} шт. — {p.price} BYN — Категория: {p.category.name}, Поставщик: {p.supplier.name}")

def create_supply_order(product_name, quantity):
    product = session.query(Product).filter_by(name=product_name).first()
    if not product:
        print("Товар не найден.")
        return
    order = SupplyOrder(product=product, quantity=quantity)
    product.quantity += quantity  # Обновление количества на складе
    session.add(order)
    session.commit()
    print("Заказ на поставку создан.")

def main_menu():
    while True:
        print("\n--- Система управления инвентарем ---")
        print("1. Добавить товар")
        print("2. Изменить товар")
        print("3. Удалить товар")
        print("4. Заказ на поставку")
        print("5. Найти товары по категории")
        print("6. Поиск по имени")
        print("7. Показать отчет по складу")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Название товара: ")
            quantity = int(input("Количество: "))
            price = float(input("Цена: "))
            category = input("Категория: ")
            supplier = input("Поставщик: ")
            add_product(name, quantity, price, category, supplier)

        elif choice == '2':
            name = input("Введите название товара для редактирования: ")
            edit_product(name)

        elif choice == '3':
            name = input("Введите название товара для удаления: ")
            delete_product(name)

        elif choice == '4':
            name = input("Название товара: ")
            quantity = int(input("Количество для заказа: "))
            create_supply_order(name, quantity)

        elif choice == '5':
            cat = input("Введите название категории: ")
            find_products_by_category(cat)

        elif choice == '6':
            model_choice = input("Что ищем? (product/supplier): ").lower()
            name_part = input("Часть названия: ")
            if model_choice == 'product':
                search_by_name(Product, name_part)
            elif model_choice == 'supplier':
                search_by_name(Supplier, name_part)
            else:
                print("Неверный выбор.")

        elif choice == '7':
            warehouse_report()

        elif choice == '8':
            print("Выход.")
            break
        else:
            print("Неверный выбор.")